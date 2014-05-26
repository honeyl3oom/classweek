# -*- coding: utf-8 -*-
import json
from datetime import datetime, timedelta
import time
import calendar

from classweek import const
from classweek.const import ITEM_COUNT_IN_PAGE, \
    WEEKDAY_CONVERT_TO_NUMBER_OR_STRING, WEEKDAY_CONVERT_TO_KOREAN, PAYMENT_STATE_TO_KOREAN

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from django.db import IntegrityError
from classes.models import Category, Company, CompanyReview, CompanyImage,\
    SubCategory, Classes, ClassesInquire, Schedule, SubCategoryRecommend, ClassesRecommend,\
    Promotion, PromotionDetail

from datetime import datetime
from time import strftime

from foradmin.models import Purchase, ApiLog
from classweek.common_method import send_email
import urllib, urllib2
import math
import logging

logger = logging.getLogger(__name__)

def helper_rename_list_of_dict_keys(list_object, rename_key_dict):
    for list_item in list_object:
        helper_rename_dict_keys(list_item, rename_key_dict)


def helper_rename_dict_keys( dict_object, rename_key_dict ):
    for before_rename, after_rename in rename_key_dict.iteritems():
        dict_object[after_rename] = dict_object.pop( before_rename )


def _make_json_response(is_success, error_message, error_code = 0 , data = None):
    return_value = {}
    if is_success:
        return_value['result'] = const.RESPONSE_STR_SUCCESS
    else:
        return_value['result'] = const.RESPONSE_STR_FAIL
    return_value['error_message'] = error_message
    return_value['error_code'] = error_code
    if data is not None:
        return_value['data'] = data

    return return_value


def _http_json_response(error, data=[], error_code = 0):
    if error is None:
        return HttpResponse(json.dumps( _make_json_response( True, None, error_code, data ) , ensure_ascii=False ), content_type="application/json; charset=utf-8" )
    else:
        return HttpResponse(json.dumps( _make_json_response( False, error, error_code, data ) , ensure_ascii=False ), content_type="application/json; charset=utf-8" )

def _http_response_by_json(error, json_={}):
    if error is None:
        json_.update({
            'result': 'success'
        })
    else:
        json_.update({
            'result': 'fail',
            'error_code': error,
            'error_message': const.ERROR_CODE_AND_MESSAGE_DICT[error]
        })

    return HttpResponse(json.dumps(json_, ensure_ascii=False), content_type="application/json; charset=utf-8")

def _check_promotion():
    now_ = datetime.now()
    promotions = Promotion.objects.filter( start_date__lte=now_, end_date__gte=now_, daily_start_time__lte=now_, daily_end_time__gte=now_).all()

    if len(promotions)>0:
        promotion = promotions[0]

        total_count = promotion.get_promotion_details.count()
        today_count = promotion.get_promotion_details.filter(created__day=now_.day).count()

        if promotion.total_maximum_count>total_count and promotion.daily_maximum_count>today_count:
            return promotion, const.CODE_IN_PROMOTION, promotion.discount_percentage
        else:
            return promotion, const.CODE_TODAY_PROMOTION_END, 0

    return None, const.CODE_NOT_IN_PROMOTION, 0


@csrf_exempt
def promotion_view(request):

    promotion_obj, resp, percentage = _check_promotion()

    return _http_response_by_json(None, {
        'data_code': resp,
        'data_message': const.PROMOTION_CODE_AND_MESSAGE_DICT[resp]
    })

@csrf_exempt
def get_sub_category_list_view(request, category_name ):
    try:
        sub_categorys = list(Category.objects.select_related('get_subcategorys').get(name=category_name).
                             get_subcategorys.order_by('order_priority_number').values('id', 'name', 'category_id', 'name_kor',
                                                                                       'description', 'image_url'))
        for sub_category in sub_categorys:
            sub_category['image_url'] = 'http://' + request.get_host() + sub_category['image_url'] if len(sub_category['image_url'])>0 else ''

        return _http_json_response(None, sub_categorys)
    except ObjectDoesNotExist:
        return _http_json_response(const.ERROR_CATEGORY_NAME_DOES_NOT_EXIST, None , const.CODE_ERROR_CATEGORY_NAME_DOES_NOT_EXIST)

# address, weekday, time( morning, .. ), price ( by month )
@csrf_exempt
def get_classes_list_view(request, category_name, subcategory_name, page_num='1'):

    page_num = int(page_num)

    try:
        classes = SubCategory.objects.select_related('get_classes', ).get(name=subcategory_name).get_classes

        location_filter = request.POST.get('location', None)
        price_filter = request.POST.get('price', None)
        weekday_filter = request.POST.get('weekday', None)
        start_time_filter_express_by_string = request.POST.get('time', None)

        # filter out only if there is any in 'location' param
        if location_filter is not None:
            classes = classes.filter(company__zone=request.POST.get('location', None))

        # filter out only if there is any in 'price' param
        if price_filter is not None:
            classes = classes.filter(price_of_month__lte=request.POST.get('price', None))

        classes = classes.select_related('get_schedules', 'company', ).all()

        classes_list = []

        promotion_obj, promotion_resp, promotion_percentage = _check_promotion()

        for classes_item in classes:

            company = classes_item.company
            schedules = classes_item.get_schedules.all()

            item = {}
            item.update({
                'id': classes_item.id,
                'title': classes_item.title,
                'company': company.name,
                'nearby_station': company.nearby_station,
                'price_of_day': classes_item.price_of_one_day,
                'count_of_month': classes_item.count_of_month,
                'image_url': 'http://' + request.get_host() + classes_item.company.thumbnail_image_url if len(classes_item.company.thumbnail_image_url)>0 else '',
                'original_price_of_month': classes_item.price_of_one_day*classes_item.count_of_month,
                'discount_price_of_month': classes_item.price_of_month,
                'discount_rate': round(100 - classes_item.price_of_month*100.0/(classes_item.price_of_one_day*classes_item.count_of_month))
            })

            if promotion_resp is const.CODE_IN_PROMOTION:
                item.update({
                    'original_price_of_month': classes_item.price_of_month,
                    'discount_price_of_month': math.ceil(classes_item.price_of_month*promotion_percentage/100/1000.0)*1000,
                    'discount_rate': promotion_percentage
                })

            for schedule in schedules:
                item_detail = item.copy()

                weekday_list_express_by_string = schedule.weekday_list.replace(' ','').split(',')

                # filter out only if there is any in 'weekday' param
                is_excluded_by_weekday = False
                if weekday_filter is not None:
                    for i in range(len(weekday_list_express_by_string)):
                        if not(str(weekday_filter).__contains__(str(WEEKDAY_CONVERT_TO_NUMBER_OR_STRING[weekday_list_express_by_string[i]]))):
                            is_excluded_by_weekday = True
                            break
                if is_excluded_by_weekday:
                    continue

                # get start time
                start_time_list = schedule.start_time_list.split(',')
                # filter out only if there is any in 'time' param
                is_excluded_by_start_time = False
                if start_time_filter_express_by_string is not None:
                    for i in range(len(start_time_list)):
                        time_object = time.strptime( start_time_list[i], "%H:%M:%S")

                        is_contains_in_time_filter = False

                        if "0" in start_time_filter_express_by_string:
                            if 6 <= time_object.tm_hour < 12:
                                is_contains_in_time_filter = True

                        if is_contains_in_time_filter is False and "1" in start_time_filter_express_by_string:
                            if 12 <= time_object.tm_hour < 18:
                                is_contains_in_time_filter = True

                        if is_contains_in_time_filter is False and "2" in start_time_filter_express_by_string:
                            if 18 <= time_object.tm_hour < 24:
                                is_contains_in_time_filter = True

                        if is_contains_in_time_filter is False:
                            is_excluded_by_start_time = True
                            break
                if is_excluded_by_start_time:
                    continue

                times = []

                for i in range(len(weekday_list_express_by_string)):
                    if len(start_time_list[i])<=4:
                        start_time_list[i] = start_time_list[i]+':00'

                    times.append(WEEKDAY_CONVERT_TO_KOREAN[weekday_list_express_by_string[i]].decode('utf-8') + " : " +
                                 time.strftime('%p %I시 %M분', time.strptime(start_time_list[i], '%H:%M:%S')).replace('PM', '오후').replace('AM', '오전').decode('utf-8'))

                item_detail.update({
                    'times': times,
                    'item_for_order': calendar.timegm(datetime.strptime(start_time_list[0], '%H:%M:%S').timetuple()),
                    'duration': schedule.duration.strftime("%H시간%M분").decode('utf-8'),
                    'schedule_id': schedule.id
                })

                classes_list.append(item_detail)

        classes_list = sorted(classes_list, key=lambda k: k['item_for_order'])

        return _http_json_response( None, classes_list[(page_num-1)*ITEM_COUNT_IN_PAGE: page_num*ITEM_COUNT_IN_PAGE ] )
        # else:
        #     return _http_json_response( const.ERROR_SUBCATEGORY_NAME_DOES_NOT_EXIST, None , const.CODE_ERROR_SUBCATEGORY_NAME_DOES_NOT_EXIST )


    except ObjectDoesNotExist as e:
        return _http_response_by_json(const.CODE_ERROR_SUBCATEGORY_NAME_DOES_NOT_EXIST)

@csrf_exempt
def getClassesDetail_view( request, classes_id, schedule_id ):
    classes = Classes.objects.select_related('company', 'get_images', ).get(id=classes_id)
    company = classes.company
    schedule = Schedule.objects.get(id = schedule_id)

    classes_detail = {}

    personal_or_group = classes.personal_or_group
    if personal_or_group == 'personal':
        lesson_type = '개인 레슨'
    elif personal_or_group == 'group':
        lesson_type = '그룹 레슨(정원 ' + str(classes.maximum_number_of_enrollment) + '명)'

    facilities_information = company.facility_information

    classes_detail.update({
        'id': classes.id,
        'schedule_id': schedule.id,
        'company_id': company.id,
        'title': classes.title,
        'image_url': 'http://' + request.get_host() + company.thumbnail_image_url if len(company.thumbnail_image_url)>0 else '',
        'description': classes.description,
        'company': company.name,
        'person_or_group': classes.personal_or_group,
        'price_of_day': classes.price_of_one_day,
        'count_of_week': classes.count_of_week,
        'count_of_month': classes.count_of_month,
        'original_price_of_month': classes.price_of_one_day * classes.count_of_month,
        'discount_price_of_month': classes.price_of_month,
        'discount_rate': round(100 - classes.price_of_month*100.0/(classes.price_of_one_day*classes.count_of_month)),
        'address': company.address,
        'nearby_station': company.nearby_station,
        'curriculum_in_first_week': classes.curriculum_in_first_week.replace('\\n', '\n'),
        'curriculum_in_second_week': classes.curriculum_in_second_week.replace('\\n', '\n'),
        'curriculum_in_third_week': classes.curriculum_in_third_week.replace('\\n', '\n'),
        'curriculum_in_fourth_week': classes.curriculum_in_fourth_week.replace('\\n', '\n'),
        'curriculum_in_fifth_week': classes.curriculum_in_fifth_week.replace('\\n', '\n'),
        'lesson_type': lesson_type.decode('utf-8'),
        'preparation': classes.preparation,
        'refund_info': company.refund_information,
        'company_introduction': company.introduction,
        ### facility_infomation ###
        'toilet': facilities_information.__contains__('toilet'),
        'fitting_room': facilities_information.__contains__('fitting_room'),
        'shower_stall': facilities_information.__contains__('shower_stall'),
        'locker': facilities_information.__contains__('locker'),
        'parking_lot': facilities_information.__contains__('parking_lot'),
        'practice_room': facilities_information.__contains__('practice_room'),
        'instrument_rental': facilities_information.__contains__('instrument_rental')
    })

    promotion_obj, promotion_resp, promotion_percentage = _check_promotion()
    if promotion_resp is const.CODE_IN_PROMOTION:
        classes_detail.update({
            'original_price_of_month': classes.price_of_month,
            'discount_price_of_month': math.ceil(classes.price_of_month*promotion_percentage/100/1000.0)*1000,
            'discount_rate': promotion_percentage
        })

    ### good and bad review ###
    # good_representing_reviews = company.get_company_reviews.filter(is_representing_reivew=True, score__gt=3).order_by('-score').all()[:3]
    good_representing_reviews = company.get_company_reviews.filter(score__gt=3).order_by('-score').all()[:3]
    # bad_representing_reviews = company.get_company_reviews.filter(is_representing_reivew=True, score__lte=3).order_by('score').all()[:3]
    bad_representing_reviews = company.get_company_reviews.filter(score__lte=3, score__gt=0).order_by('score').all()[:3]

    good_reviews = []
    for good_representing_review in good_representing_reviews:
        good_reviews.append({
            'contents':good_representing_review.contents.replace('\r',''),
            'score':good_representing_review.score,
            'datetime': good_representing_review.created.strftime('%y-%m-%d %H:%M').decode('utf-8')
        })

    bad_reviews = []
    for bad_representing_review in bad_representing_reviews:
        bad_reviews.append({
            'contents': bad_representing_review.contents.replace('\r',''),
            'score': bad_representing_review.score,
            'datetime': bad_representing_review.created.strftime('%y-%m-%d %H:%M').decode('utf-8')
        })

    classes_detail.update({
        'good_reviews': good_reviews,
        'bad_reviews': bad_reviews
    })


    ### detail image list ###
    images = company.get_company_images.all()
    detail_images = []
    for image in images:
        if len(image.image_url) > 0:
            detail_images.append('http://' + request.get_host() + image.image_url) if len(image.image_url)>0 else ''

    classes_detail.update({
        'detail_image_url': detail_images
    })

    ### time list, duration ###
    weekday_express_by_string_list = schedule.weekday_list.replace(' ','').split(',')
    start_time_express_by_string_list = schedule.start_time_list.split(',')

    times = []
    for i in range(len(weekday_express_by_string_list)):
        times.append(WEEKDAY_CONVERT_TO_KOREAN[weekday_express_by_string_list[i]].decode('utf-8') + " : " +
                     time.strftime('%p %I시 %M분', time.strptime(start_time_express_by_string_list[i], '%H:%M:%S')).replace('PM', '오후').replace('AM', '오전').decode('utf-8'))

    classes_detail.update({
        'times': times,
        'duration': schedule.duration.strftime("%H시간%M분").decode('utf-8')
    })

    ### create one month schedule ###
    today = datetime.today()
    timedelta_from_today = timedelta()
    today_weekday = today.weekday()

    current_weekday_position = 0
    for i in range( len(weekday_express_by_string_list ) ):
        if today_weekday <= WEEKDAY_CONVERT_TO_NUMBER_OR_STRING[weekday_express_by_string_list[i]]:
            current_weekday_position = i
            break

    one_month_schedule = []
    for i in range(4):

        for j in range(current_weekday_position, len(weekday_express_by_string_list ) ):
            if (today+timedelta_from_today).weekday() < WEEKDAY_CONVERT_TO_NUMBER_OR_STRING[weekday_express_by_string_list[j]]:
                timedelta_from_today = timedelta(days=timedelta_from_today.days+WEEKDAY_CONVERT_TO_NUMBER_OR_STRING[weekday_express_by_string_list[j]]-(today+timedelta_from_today).weekday())
            else:
                timedelta_from_today = timedelta(days=7+timedelta_from_today.days+WEEKDAY_CONVERT_TO_NUMBER_OR_STRING[weekday_express_by_string_list[j]]-(today+timedelta_from_today).weekday())

            start_date = today+timedelta_from_today
            if j == 0:
                end_date = start_date + timedelta(days=21+WEEKDAY_CONVERT_TO_NUMBER_OR_STRING[weekday_express_by_string_list[len(weekday_express_by_string_list)-1]] - start_date.weekday())
            else:
                end_date = start_date + timedelta(days=28+WEEKDAY_CONVERT_TO_NUMBER_OR_STRING[weekday_express_by_string_list[j-1]] - start_date.weekday())

            one_month_schedule.append( {
                'start_date_time': str(start_date.month)+"-"+str(start_date.day)+"("+WEEKDAY_CONVERT_TO_KOREAN[WEEKDAY_CONVERT_TO_NUMBER_OR_STRING[start_date.weekday()]].decode('utf-8')+") " + time.strftime('%p %I시 %M분', time.strptime(start_time_express_by_string_list[j], '%H:%M:%S')).replace('PM', '오후').replace('AM', '오전').decode('utf-8'),
                'start_date_time_unprocessed': str(start_date),
                'end_date_time': str(end_date.month)+"-"+str(end_date.day)+"("+WEEKDAY_CONVERT_TO_KOREAN[WEEKDAY_CONVERT_TO_NUMBER_OR_STRING[end_date.weekday()]].decode('utf-8')+") " + time.strftime('%p %I시 %M분', time.strptime(start_time_express_by_string_list[j], '%H:%M:%S')).replace('PM', '오후').replace('AM', '오전').decode('utf-8'),
                'end_date_time_unprocessed': str(end_date)
            })

        for j in range( 0, current_weekday_position ):
            if (today+timedelta_from_today).weekday() < WEEKDAY_CONVERT_TO_NUMBER_OR_STRING[weekday_express_by_string_list[j]]:
                timedelta_from_today = timedelta(days=timedelta_from_today.days+WEEKDAY_CONVERT_TO_NUMBER_OR_STRING[weekday_express_by_string_list[j]]-(today+timedelta_from_today).weekday())
            else:
                timedelta_from_today = timedelta(days=7+timedelta_from_today.days+WEEKDAY_CONVERT_TO_NUMBER_OR_STRING[weekday_express_by_string_list[j]]-(today+timedelta_from_today).weekday())

            start_date = today+timedelta_from_today
            if j == 0:
                end_date = start_date + timedelta(days=21+WEEKDAY_CONVERT_TO_NUMBER_OR_STRING[weekday_express_by_string_list[len(weekday_express_by_string_list)-1]] - start_date.weekday())
            else:
                end_date = start_date + timedelta(days=28+WEEKDAY_CONVERT_TO_NUMBER_OR_STRING[weekday_express_by_string_list[j-1]] - start_date.weekday())

            one_month_schedule.append( {
                'start_date_time':str(start_date.month)+"-"+str(start_date.day)+"("+WEEKDAY_CONVERT_TO_KOREAN[WEEKDAY_CONVERT_TO_NUMBER_OR_STRING[start_date.weekday()]].decode('utf-8')+") " + time.strftime('%p %I시 %M분', time.strptime(start_time_express_by_string_list[j], '%H:%M:%S')).replace('PM', '오후').replace('AM', '오전').decode('utf-8'),
                'start_date_time_unprocessed': str(start_date),
                'end_date_time':str(end_date.month)+"-"+str(end_date.day)+"("+WEEKDAY_CONVERT_TO_KOREAN[WEEKDAY_CONVERT_TO_NUMBER_OR_STRING[end_date.weekday()]].decode('utf-8')+") " + time.strftime('%p %I시 %M분', time.strptime(start_time_express_by_string_list[j], '%H:%M:%S')).replace('PM', '오후').replace('AM', '오전').decode('utf-8'),
                'end_date_time_unprocessed': str(end_date)
            })

    classes_detail.update({
        'one_month_schedule':one_month_schedule
    })

    return _http_json_response(None, classes_detail )

@csrf_exempt
def review_view(request, company_id, page_num=1):
    page_num=int(page_num)
    reviews = Company.objects.get(id=company_id).get_company_reviews.all()[(page_num-1)*10:page_num*10]
    data = []
    for review in reviews:
        data.append({
            'contents':review.contents.replace('\r',''),
            'score':review.score,
            'datetime': review.created.strftime('%y-%m-%d %H:%M').decode('utf-8')
        })

    return _http_response_by_json(None, {
        'data': data
    })

@csrf_exempt
def inquire_view(request, classes_id):
    if not(request.user.is_authenticated()):
        return HttpResponse(json.dumps(_make_json_response( False, const.ERROR_HAVE_TO_LOGIN, const.CODE_ERROR_HAVE_TO_LOGIN)), content_type="application/json")
    else:
        classes_inquire = ClassesInquire( classes_id = classes_id, user = request.user, content= request.POST.get('content') )
        try:
            classes_inquire.save()
        except IntegrityError:
            return HttpResponse( json.dumps( _make_json_response( False, const.ERROR_CLASSES_INQUIRE_FAIL, const.CODE_ERROR_CLASSES_INQUIRE_FAIL ) ), content_type="application/json" )

        send_email('classweek:inquire',
                   'username:\n' + request.user.username + '\ncontent:\n' + request.POST.get('content'))
        return HttpResponse( json.dumps( _make_json_response( True, None ) ), content_type="application/json" )

@csrf_exempt
def recommend_subcategory_view(request):
    sub_category_recommends = list ( SubCategoryRecommend.objects.values('image_url'))

    for sub_category_recommend in sub_category_recommends:
        sub_category_recommend['image_url'] = 'http://' + request.get_host() + sub_category_recommend['image_url'] if len(sub_category_recommend['image_url'])>0 else ''

    return _http_json_response(None, sub_category_recommends)

@csrf_exempt
def recommend_classes_view(request):
    logger.info( 'def recommend_classes_view(request):' )
    classes_pks = ClassesRecommend.objects.values_list('classes', flat=True)
    schedule_pks = ClassesRecommend.objects.values_list('schedule', flat=True)
    classes = Classes.objects.filter(pk__in=classes_pks).select_related('get_schedules', 'company', ).all()
    classes_list = []

    for classes_item in classes:
        classes_list_item = {}
        classes_list_item.update({
            'id': classes_item.id,
            'title': classes_item.title,
            'company': classes_item.company.name,
            'nearby_station': classes_item.company.nearby_station,
            'count_of_month': classes_item.count_of_month,
            'price_of_day': classes_item.price_of_one_day,
            'original_price_of_month': classes_item.price_of_one_day*classes_item.count_of_month,
            'discount_price_of_month': classes_item.price_of_month,
            'image_url': 'http://' + request.get_host() + classes_item.company.thumbnail_image_url if len(classes_item.company.thumbnail_image_url)>0 else '',
            'discount_rate': round(100 - classes_item.price_of_month*100.0/(classes_item.price_of_one_day*classes_item.count_of_month))
        })

        promotion_obj, promotion_resp, promotion_percentage = _check_promotion()
        if promotion_resp is const.CODE_IN_PROMOTION:
            classes_list_item.update({
                'original_price_of_month': classes_item.price_of_month,
                'discount_price_of_month': math.ceil(classes_item.price_of_month*promotion_percentage/100/1000.0)*1000,
                'discount_rate': promotion_percentage
            })

        schedules = classes_item.get_schedules.filter(pk__in=schedule_pks).all()
        for schedule in schedules:
            classes_list_item_detail = classes_list_item.copy()

            # get weekday
            weekday_express_by_string_list = schedule.weekday_list.replace(' ','').split(',')

            # get start time
            start_time_list = schedule.start_time_list.split(',')

            times = []
            for i in range(len(weekday_express_by_string_list)):
                weekday_express_by_korean = WEEKDAY_CONVERT_TO_KOREAN[weekday_express_by_string_list[i]]
                start_time_string_expressed_by_custom_style = time.strftime('%p %I시 %M분', time.strptime(start_time_list[i], '%H:%M:%S')).replace('PM', '오후').replace('AM', '오전').decode('utf-8')
                times.append(weekday_express_by_korean.decode('utf-8') + " : " + start_time_string_expressed_by_custom_style)

            classes_list_item_detail.update({
                'times': times,
                'duration': schedule.duration.strftime("%H시간%M분").decode('utf-8'),
                'schedule_id': schedule.id
            })

            classes_list.append(classes_list_item_detail)

    return _http_json_response(None, classes_list)

@csrf_exempt
def now_taking_view(request):

    now_taking_list = []

    if request.user.is_authenticated():
        purchases = Purchase.objects.filter(user=request.user, class_end_datetime__gte=datetime.now()).all()
    else:
        return _http_json_response(None, now_taking_list)

    for purchase in purchases:
        classes = purchase.classes
        schedule = purchase.schedule

        title = classes.title
        image_url = 'http://' + request.get_host() + classes.company.thumbnail_image_url if len(classes.company.thumbnail_image_url)>0 else ''

        weekday_before_split_expressed_by_string = schedule.weekday_list
        weekday_list_expressed_by_string = weekday_before_split_expressed_by_string.split(',')
        start_time_before_split_expressed_by_string = schedule.start_time_list
        start_time_list_expressed_by_string = start_time_before_split_expressed_by_string.split(',')
        duration_time = schedule.duration

        time_string = ''

        if len(weekday_list_expressed_by_string) == len(start_time_list_expressed_by_string):
            for i in range(len(weekday_list_expressed_by_string)):
                if i != 0:
                    time_string += ', '
                weekday_expressed_by_korean = WEEKDAY_CONVERT_TO_KOREAN[weekday_list_expressed_by_string[i]]
                start_time = datetime.strptime(start_time_list_expressed_by_string[i], '%H:%M:%S').time()
                end_time = (datetime.combine( datetime.today(), start_time) +
                            timedelta(hours=duration_time.hour, minutes=duration_time.minute)).time()

                time_string += weekday_expressed_by_korean + start_time.strftime(' %H:%M-') + end_time.strftime('%H:%M')

        else:
            pass

        start_datetime = purchase.class_start_datetime
        end_datetime = purchase.class_end_datetime
        current_state = purchase.state

        now_taking_item = {
            'title': title,
            'image_url': image_url,
            'time': time_string.decode('utf-8'),
            'start_datetime': (start_datetime.strftime("%Y-%m-%d ") +
                              WEEKDAY_CONVERT_TO_KOREAN[WEEKDAY_CONVERT_TO_NUMBER_OR_STRING[int(start_datetime.strftime("%w"))]]).decode('utf-8'),
            'end_datetime': (end_datetime.strftime("%Y-%m-%d ") +
                            WEEKDAY_CONVERT_TO_KOREAN[WEEKDAY_CONVERT_TO_NUMBER_OR_STRING[int(end_datetime.strftime("%w"))]]).decode('utf-8'),
            'current_state': PAYMENT_STATE_TO_KOREAN[current_state].decode('utf-8')
        }

        now_taking_list.append(now_taking_item)

    return _http_json_response(None, now_taking_list)

@csrf_exempt
def took_before_view(request):

    before_taking_list = []


    if request.user.is_authenticated():
        purchase_list = Purchase.objects.filter(user=request.user, class_end_datetime__lt=datetime.now()).all()
    else:
        return _http_json_response(None, before_taking_list)



    for purchase in purchase_list:
        classes = purchase.classes
        schedule = purchase.schedule

        title = classes.title
        image_url = 'http://' + request.get_host() + classes.company.thumbnail_image_url  if len(classes.company.thumbnail_image_url)>0 else ''
        weekday_before_split_expressed_by_string = schedule.weekday_list
        weekday_list_expressed_by_string = weekday_before_split_expressed_by_string.split(',')
        start_time_before_split_expressed_by_string = schedule.start_time_list
        start_time_list_expressed_by_string = start_time_before_split_expressed_by_string.split(',')
        duration_time = schedule.duration

        time_string = ''

        if len(weekday_list_expressed_by_string) == len(start_time_list_expressed_by_string):
            for i in range(len(weekday_list_expressed_by_string)):
                if i != 0:
                    time_string += ', '
                weekday_expressed_by_korean = WEEKDAY_CONVERT_TO_KOREAN[weekday_list_expressed_by_string[i]]
                start_time = datetime.strptime(start_time_list_expressed_by_string[i], '%H:%M:%S').time()
                end_time = (datetime.combine( datetime.today(), start_time) +
                            timedelta(hours=duration_time.hour, minutes=duration_time.minute)).time()

                time_string += weekday_expressed_by_korean + start_time.strftime(' %H:%M-') + end_time.strftime('%H:%M')

        else:
            pass

        start_datetime = purchase.class_start_datetime
        end_datetime = purchase.class_end_datetime
        current_state = purchase.state

        before_taking_item = {
            'title': title,
            'image_url': image_url,
            'time': time_string.decode('utf-8'),
            'start_datetime': (start_datetime.strftime("%Y-%m-%d ") +
                              WEEKDAY_CONVERT_TO_KOREAN[WEEKDAY_CONVERT_TO_NUMBER_OR_STRING[int(start_datetime.strftime("%w"))]]).decode('utf-8'),
            'end_datetime': (end_datetime.strftime("%Y-%m-%d ") +
                            WEEKDAY_CONVERT_TO_KOREAN[WEEKDAY_CONVERT_TO_NUMBER_OR_STRING[int(end_datetime.strftime("%w"))]]).decode('utf-8'),
            'current_state': PAYMENT_STATE_TO_KOREAN[current_state].decode('utf-8')
        }

        before_taking_list.append(before_taking_item)

    return _http_json_response(None, before_taking_list)

def import_all_view(request):
    import_category_csv_file_view(request)
    import_sub_category_csv_file_view(request)
    import_company_csv_file_view(request)
    import_classes_csv_file_view(request)
    import_schedule_csv_file_view(request)
    import_sub_category_recommend_csv_file_view(request)

    return _http_json_response(None)

import csv

def import_category_csv_file_view(request):
    with open('./classes/resource/model/csv/category_model.csv', 'rb') as f:
        reader = csv.reader(f,  delimiter='|')
        is_first = True

        for row in reader:
            if is_first:
                is_first = False
                continue
            Category.objects.get_or_create(
                name=row[0])

    return _http_json_response(None)


def import_sub_category_csv_file_view(request):
    with open('./classes/resource/model/csv/sub_category_model.csv', 'rb') as f:
        reader = csv.reader(f,  delimiter='|')
        is_first = True

        for row in reader:
            if is_first:
                is_first = False
                continue

            SubCategory.objects.get_or_create(
                name=unicode(row[0], 'euc-kr'),
                category=Category.objects.get(name=unicode(row[1], 'euc-kr')),
                name_kor=unicode(row[2], 'euc-kr'),
                description=unicode(row[3], 'euc-kr'),
                image_url=unicode(row[4], 'euc-kr'))

    return _http_json_response(None)


def import_company_csv_file_view(request):
    logger.info('def import_company_csv_file_view(request):')
    with open('./classes/resource/model/csv/company_model.csv', 'rb') as f:
        reader = csv.reader(f,  delimiter='|')
        is_first = True

        for row in reader:
            if is_first:
                is_first = False
                continue

            if Company.objects.filter(name=unicode(row[0], 'euc-kr')).count()>0 :
                Company.objects.filter(name=unicode(row[0], 'euc-kr')).update(
                    contact=unicode(row[1], 'euc-kr'),
                    address=unicode(row[2], 'euc-kr'),
                    zone=unicode(row[3], 'euc-kr'),
                    nearby_station=unicode(row[4], 'euc-kr'),
                    introduction=unicode(row[5], 'euc-kr'),
                    refund_information=unicode(row[6], 'euc-kr'),
                    facility_information=unicode(row[7], 'euc-kr'),
                    naver_object_id=unicode(row[8], 'euc-kr'),
                    thumbnail_image_url=unicode(row[9], 'euc-kr'))
            else:
                Company.objects.get_or_create(
                    name=unicode(row[0], 'euc-kr'),
                    contact=unicode(row[1], 'euc-kr'),
                    address=unicode(row[2], 'euc-kr'),
                    zone=unicode(row[3], 'euc-kr'),
                    nearby_station=unicode(row[4], 'euc-kr'),
                    introduction=unicode(row[5], 'euc-kr'),
                    refund_information=unicode(row[6], 'euc-kr'),
                    facility_information=unicode(row[7], 'euc-kr'),
                    naver_object_id=unicode(row[8], 'euc-kr'),
                    thumbnail_image_url=unicode(row[9], 'euc-kr'))

            company = Company.objects.get(name=unicode(row[0], 'euc-kr'))

            for i in range(10, len(row)):
                if len(row[i]) > 0:
                    CompanyImage.objects.get_or_create(
                        company=company,
                        image_url=unicode(row[i], 'euc-kr')
                    )
                else:
                    break

            if len(company.naver_object_id)>0:
                scrap_company_review_in_naver(company.naver_object_id)

    return _http_json_response(None)


def import_classes_csv_file_view(request):
    logger.info('def import_classes_csv_file_view(request):')
    with open('./classes/resource/model/csv/classes_model.csv', 'rb') as f:
        reader = csv.reader(f,  delimiter='|')
        is_first = True

        for row in reader:
            if is_first:
                is_first = False
                continue

            try:
                sub_category = SubCategory.objects.get(name=unicode(row[1], 'euc-kr'))
            except Exception, e:
                logger.error(unicode(row[1], 'euc-kr'), e)

            try:
                company = Company.objects.get(name=unicode(row[2], 'euc-kr'))
            except Exception, e:
                logger.error(unicode(row[2], 'euc-kr'), e)

            if Classes.objects.filter(
                title=unicode(row[0], 'euc-kr'),
                sub_category=sub_category,
                company=company,
                personal_or_group=unicode(row[4], 'euc-kr')).count()>0:

                Classes.objects.filter(
                    title=unicode(row[0], 'euc-kr'),
                    sub_category=sub_category,
                    company=company,
                    personal_or_group=unicode(row[4], 'euc-kr')).update(
                    description=unicode(row[3], 'euc-kr'),
                    is_allowed_one_day=unicode(row[5], 'euc-kr'),
                    price_of_one_day=unicode(row[6], 'euc-kr'),
                    count_of_week=unicode(row[7], 'euc-kr'),
                    count_of_month=unicode(row[8], 'euc-kr'),
                    price_of_month=unicode(row[9], 'euc-kr'),
                    preparation=unicode(row[10], 'euc-kr'),
                    maximum_number_of_enrollment=unicode(row[11], 'euc-kr'),
                    curriculum_in_first_week=unicode(row[12], 'euc-kr'),
                    curriculum_in_second_week=unicode(row[13], 'euc-kr'),
                    curriculum_in_third_week=unicode(row[14], 'euc-kr'),
                    curriculum_in_fourth_week=unicode(row[15], 'euc-kr'),
                    curriculum_in_fifth_week=row[16] if row[16] is '' else unicode(row[16], 'euc-kr'))
            else:
                Classes.objects.get_or_create(
                    title=unicode(row[0], 'euc-kr'),
                    sub_category=sub_category,
                    company=company,
                    description=unicode(row[3], 'euc-kr'),
                    personal_or_group=unicode(row[4], 'euc-kr'),
                    is_allowed_one_day=unicode(row[5], 'euc-kr'),
                    price_of_one_day=unicode(row[6], 'euc-kr'),
                    count_of_week=unicode(row[7], 'euc-kr'),
                    count_of_month=unicode(row[8], 'euc-kr'),
                    price_of_month=unicode(row[9], 'euc-kr'),
                    preparation=unicode(row[10], 'euc-kr'),
                    maximum_number_of_enrollment=unicode(row[11], 'euc-kr'),
                    curriculum_in_first_week=unicode(row[12], 'euc-kr'),
                    curriculum_in_second_week=unicode(row[13], 'euc-kr'),
                    curriculum_in_third_week=unicode(row[14], 'euc-kr'),
                    curriculum_in_fourth_week=unicode(row[15], 'euc-kr'),
                    curriculum_in_fifth_week=row[16] if row[16] is '' else unicode(row[16], 'euc-kr'))

    return _http_json_response(None)

def import_schedule_csv_file_view(request):
    logger.info('def import_schedule_csv_file_view(request):')
    with open('./classes/resource/model/csv/classes_model.csv', 'rb') as f:
        reader = csv.reader(f,  delimiter='|')
        is_first = True

        for row in reader:
            if is_first:
                is_first = False
                continue

            try:
                sub_category = SubCategory.objects.get(name=unicode(row[1], 'euc-kr'))
            except Exception, e:
                logger.error(unicode(row[1], 'euc-kr'), e)

            try:
                company = Company.objects.get(name=unicode(row[2], 'euc-kr'))
            except Exception, e:
                logger.error(unicode(row[2], 'euc-kr'))
                logger.error(e)

            try:
                classes = Classes.objects.get(
                    title=unicode(row[0], 'euc-kr'),
                    sub_category=sub_category,
                    company=company,
                    personal_or_group=unicode(row[4], 'euc-kr'))

                weekday_list=unicode(row[17], 'euc-kr')
                start_time_list=unicode(row[18], 'euc-kr')
                if len(weekday_list.split(',')) is not len(start_time_list.split(',')):
                    logger.error('weekday_list and start_time_list item count is not matched')
                else:
                    Schedule.objects.get_or_create(
                        classes=classes,
                        weekday_list=weekday_list,
                        start_time_list=start_time_list,
                        duration=unicode(row[19], 'euc-kr'))

            except Exception, e:
                logger.error(e)

    return _http_json_response(None)

def import_sub_category_recommend_csv_file_view(request):
    with open('./classes/resource/model/csv/sub_category_recommend_model.csv', 'rb') as f:
        reader = csv.reader(f,  delimiter='|')
        is_first = True

        for row in reader:
            if is_first:
                is_first = False
                continue

            SubCategoryRecommend.objects.get_or_create(
                image_url=row[0]
            )
    pass

def scrap_company_review_in_naver(object_id):
    url = "http://map.naver.com/comments/list_comment.nhn"
    headers = {'Referer': 'http://map.naver.com/',}
    post_params = {
        'ticket':'map1',
        'object_id': object_id,
        'page_size':'10'
    }

    page_no=1
    total_count = None
    comments = []
    while True:

        post_params.update({
            'page_no':page_no
        })
        req = urllib2.Request(url=url, data=urllib.urlencode(post_params), headers=headers)
        resp = urllib2.urlopen(req)

        try:
            resp_content = resp.read()
            resp_content = resp_content.replace("\'","\"")
            comment_dict = json.loads(resp_content)
        except Exception as e:
            logger.info(e)
            break

        comment_list = comment_dict.get('comment_list')
        total_count = comment_dict.get('total_count') if total_count == None else total_count

        comments += comment_list

        if len(comments) >= total_count :
            break

        page_no=page_no+1

    company = Company.objects.get(naver_object_id=object_id)
    for i in range(total_count):
        CompanyReview.objects.get_or_create(
            company=company,
            user=None,
            source='naver',
            contents=comments[i]['contents'],
            score=float(comments[i]['object_score']),
            created=datetime.strptime(comments[i]['registered_ymdt'][:19],"%Y-%m-%dT%H:%M:%S"))
#
@csrf_exempt
def scrap_company_review_in_naver_view(request):

    object_name_and_id_list = [
        {'name':'울림아트&이노영 기타스튜디오', 'object_id':'34714061'},
        {'name':'NG 논현 기타 Lab', 'object_id':'32786110'},
        {'name':'매치스튜디오', 'object_id':'11869806'},
        {'name':'단테보컬엔뮤직스튜디오', 'object_id':'21791136'},
        {'name':'대치기타음악교습소', 'object_id':'13147650'},
        {'name':'기타와드럼음악학원', 'object_id':'11640701'},
        {'name':'애플기타교습소', 'object_id':'13286206'},
        {'name':'서초 실용음악', 'object_id':'12770002'},
        {'name':'로코망고', 'object_id':'32382958'},
        {'name':'라브우기', 'object_id':'32397954'},
        {'name':'스마일라이프', 'object_id':'13418971'},
        {'name':'위너스댄스스쿨 강남점', 'object_id':'33989543'},
        {'name':'DMC댄스컴퍼니', 'object_id':'12771498'},
        {'name':'에이뮤즈댄스학원', 'object_id':'13197429'},
        {'name':'크레이지댄스아카데미', 'object_id':'11634274'},
        {'name':'데프댄스스쿨 강남점', 'object_id':'12948675'},
        {'name':'JW 퍼포머스쿨', 'object_id':'32582248'},
        {'name':'KM Dance Company', 'object_id':'20059178'},
        {'name':'댄스스타', 'object_id':'33963897'},
        {'name':'압구정이지댄스', 'object_id':'11677621'},
        {'name':'워너비댄스아카데미', 'object_id':'21059767'},
        {'name':'더댄스', 'object_id':'11523513'},
        {'name':'디오에이치씨', 'object_id':'12869538'},
        {'name':'YANIDANCE ACADEMY', 'object_id':'20691059'},
        {'name':'애나댄스포오스학원', 'object_id':'12774556'},
        {'name':'레츠댄스', 'object_id':'13527248'},
        {'name':'청담댄스아카데미', 'object_id':'19978106'},
        {'name':'LP댄스멀티플렉스 강남점', 'object_id':'11702455'},
        {'name':'ING댄스아카데미', 'object_id':'13490071'},
        {'name':'라인댄스 팩토리', 'object_id':'21647039'},
        {'name':'이지댄스 강남점', 'object_id':'11568543'},
        {'name':'디엠스쿨', 'object_id':'13453773'}
    ]

    url = "http://map.naver.com/comments/list_comment.nhn"
    headers = {'Referer': 'http://map.naver.com/',}
    post_params = {
        'ticket':'map1',
        'object_id': '11869806',
        'page_size':'10'
        # 'page_no':'236'
    }

    # req = urllib2.Request(url=url, data=urllib.urlencode(post_params), headers=headers)
    # resp = urllib2.urlopen(req)
    #
    # resp_content = resp.read()
    #
    #
    # print resp_content
    # resp_content = resp_content.replace("\'","\"")
    #
    # json_dict = json.loads(resp_content)
    #
    #
    # return HttpResponse( resp_content, content_type="application/json; charset=utf-8")

    page_no = 1
    total_count = None
    comments = []
    while True:
        print page_no
        post_params['page_no'] = page_no

        req = urllib2.Request(url=url, data=urllib.urlencode(post_params), headers=headers)
        resp = urllib2.urlopen(req)

        try:
            resp_content = resp.read()
            resp_content = resp_content.replace("\'","\"")
            comment_dict = json.loads(resp_content)
        except Exception as e:
            logger.info(e)
            break

        comment_list = comment_dict.get('comment_list')
        total_count = comment_dict.get('total_count') if total_count == None else total_count

        comments += comment_list

        if len(comments) >= total_count :
            break

        page_no = page_no + 1

    # for comment in comments:
    #     comment['']

    return HttpResponse( json.dumps({'comments':comments}), content_type="application/json; charset=utf-8")
