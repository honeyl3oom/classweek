# -*- coding: utf-8 -*-
import json
from datetime import datetime, timedelta
import time

from classweek import const
from classweek.const import ITEM_COUNT_IN_PAGE, WEEKDAY_CONVERT_TO_NUMBER_OR_STRING, WEEKDAY_CONVERT_TO_KOREAN

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from django.db import IntegrityError
from classes.models import Category, Company, CompanyImage,\
    SubCategory, Classes, ClassesInquire, Schedule, SubCategoryRecommend, ClassesRecommend
from foradmin.models import Purchase

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


def _http_json_response(error, data, error_code = 0):
    if error is None:
        return HttpResponse(json.dumps( _make_json_response( True, None, error_code, data ) , ensure_ascii=False ), content_type="application/json; charset=utf-8" )
    else:
        return HttpResponse(json.dumps( _make_json_response( False, error, error_code, data ) , ensure_ascii=False ), content_type="application/json; charset=utf-8" )


@csrf_exempt
def get_sub_category_list_view(request, category_name ):
    try:
        sub_categorys = list(Category.objects.select_related('get_subcategorys').get(name=category_name).
                             get_subcategorys.order_by('order_priority_number').values('id', 'name', 'category_id', 'name_kor',
                                                                                       'description', 'image_url'))
        for sub_category in sub_categorys:
            sub_category['image_url'] = 'http://' + request.get_host() + sub_category['image_url']

        return _http_json_response(None, sub_categorys)
    except ObjectDoesNotExist:
        return _http_json_response(const.ERROR_CATEGORY_NAME_DOES_NOT_EXIST, None , const.CODE_ERROR_CATEGORY_NAME_DOES_NOT_EXIST)

# location, weekday, time( morning, .. ), price ( by month )
@csrf_exempt
def getClassesList_view( request, category_name, subcategory_name, page_num = 1 ):

    print category_name, subcategory_name

    page_num = int(page_num)

    subcategory = SubCategory.objects.filter( name = subcategory_name ).select_related( 'get_classes' )
    if subcategory.exists():
        classes = subcategory.first().get_classes

        # filter out only if there is any in 'location' param
        if request.POST.get('location', None) is not None:
            classes = classes.filter( company__zone = request.POST.get('location', None))

        # filter out only if there is any in 'price' param
        if request.POST.get('price', None) is not None:
            classes = classes.filter( priceOfMonth__lte = request.POST.get('price', None) )

        classes = classes.select_related('get_schedules', 'company', ).all()
        classes_list = []

        for classes_item in classes:
            item = {}
            item.update({
                'id': classes_item.id,
                'title': classes_item.title,
                'company': classes_item.company.name,
                'nearby_station': classes_item.company.nearby_station,
                'price_of_day': classes_item.priceOfDay,
                'count_of_month': classes_item.countOfMonth,
                'original_price_of_month': classes_item.priceOfDay*classes_item.countOfMonth,
                'discount_price_of_month': classes_item.priceOfMonth,
                'image_url': 'http://' + request.get_host() + classes_item.company.thumbnail_image_url,
                'discount_rate': round(100 - classes_item.priceOfMonth*100.0/(classes_item.priceOfDay*classes_item.countOfMonth))
                })
            schedules = classes_item.get_schedules.all()
            for schedule in schedules:
                item_detail = item.copy()

                # get weekday
                weekday_express_by_string_list = schedule.dayOfWeek.split(',')
                # filter out only if there is any in 'weekday' param
                weekday_filter = request.POST.get('weekday', None)
                is_excluded_by_weekday = False
                if weekday_filter is not None:
                    for i in range(len(weekday_express_by_string_list)):
                        if not(str(weekday_filter).__contains__(str(WEEKDAY_CONVERT_TO_NUMBER_OR_STRING[weekday_express_by_string_list[i]]))):
                            is_excluded_by_weekday = True
                            break
                if is_excluded_by_weekday:
                    continue

                # get start time
                start_time_list = schedule.startTime.split(',')
                # filter out only if there is any in 'time' param
                start_time_filter_express_by_string = request.POST.get('time', None)
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

                for i in range(len(weekday_express_by_string_list)):
                    times.append(WEEKDAY_CONVERT_TO_KOREAN[weekday_express_by_string_list[i]].decode('utf-8') + " : " +
                                 time.strftime('%p %I시 %M분', time.strptime(start_time_list[i], '%H:%M:%S')).replace('PM', '오후').replace('AM', '오전').decode('utf-8'))

                item_detail.update({
                    'times': times,
                    'duration': schedule.duration.strftime("%H시간%M분").decode('utf-8'),
                    'schedule_id': schedule.id
                })

                classes_list.append(item_detail)

        return _http_json_response( None, classes_list[ (page_num-1)*ITEM_COUNT_IN_PAGE : page_num*ITEM_COUNT_IN_PAGE ] )
    else:
        return _http_json_response( const.ERROR_SUBCATEGORY_NAME_DOES_NOT_EXIST, None , const.CODE_ERROR_SUBCATEGORY_NAME_DOES_NOT_EXIST )

@csrf_exempt
def getClassesDetail_view( request, classes_id, schedule_id ):
    classes = Classes.objects.select_related('company', 'get_images' ).get( id = classes_id )
    schedule = Schedule.objects.get( id = schedule_id )

    classes_detail = {}

    classes_detail.update( {
        'id': classes.id,
        'title': classes.title,
        'company': classes.company.name,
        'nearby_station': classes.company.nearby_station,
        'address': classes.company.location,
        'person_or_group': classes.personalOrGroup,
        'description': classes.description,
        'preparation': classes.preparation,
        'refund_info': classes.refundInformation.replace('\\n', '\n'),
        'price_of_day': classes.priceOfDay,
        'original_price_of_month': classes.priceOfDay*classes.countOfMonth,
        'discount_price_of_month': classes.priceOfMonth,
        'count_of_month': classes.countOfMonth,
        'discount_rate': round(100 - classes.priceOfMonth*100.0/(classes.priceOfDay*classes.countOfMonth)),
        'image_url': 'http://' + request.get_host() + classes.company.thumbnail_image_url
    })

    facilities_information = classes.company.facilitiesInformation

    classes_detail.update({
        'toilet': facilities_information.__contains__('toilet'),
        'fitting_room': facilities_information.__contains__('fitting_room'),
        'shower_stall': facilities_information.__contains__('shower_stall'),
        'locker': facilities_information.__contains__('locker'),
        'parking_lot': facilities_information.__contains__('parking_lot'),
        'practice_room': facilities_information.__contains__('practice_room'),
        'instrument_rental': facilities_information.__contains__('instrument_rental')
    })

    images = classes.company.get_company_images.all()
    detail_images = []
    for image in images:
        if len(image.image_url) > 0:
            detail_images.append('http://' + request.get_host() + image.image_url)

    classes_detail.update({
        'detail_image_url': detail_images
    })

    weekday_express_by_string_list = schedule.dayOfWeek.split(',')
    start_time_express_by_string_list = schedule.startTime.split(',')

    times = []
    for i in range(len(weekday_express_by_string_list)):
        times.append(WEEKDAY_CONVERT_TO_KOREAN[weekday_express_by_string_list[i]].decode('utf-8') + " : " +
                     time.strftime('%p %I시 %M분', time.strptime(start_time_express_by_string_list[i], '%H:%M:%S')).replace('PM', '오후').replace('AM', '오전').decode('utf-8'))

    classes_detail.update({
        'times': times,
        'duration': schedule.duration.strftime("%H시간%M분").decode('utf-8'),
        'schedule_id': schedule.id
    })

    today = datetime.today()
    today_year = today.year
    today_month = today.month
    today_day = today.day
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
            if (today+timedelta_from_today).weekday() <= WEEKDAY_CONVERT_TO_NUMBER_OR_STRING[weekday_express_by_string_list[j]]:
                timedelta_from_today = timedelta(days=timedelta_from_today.days+WEEKDAY_CONVERT_TO_NUMBER_OR_STRING[weekday_express_by_string_list[j]]-(today+timedelta_from_today).weekday())
            else:
                timedelta_from_today = timedelta(days=7+timedelta_from_today.days+WEEKDAY_CONVERT_TO_NUMBER_OR_STRING[weekday_express_by_string_list[j]]-(today+timedelta_from_today).weekday())

            start_date = today+timedelta_from_today
            if j == 0:
                end_date = start_date + timedelta(days=21+WEEKDAY_CONVERT_TO_NUMBER_OR_STRING[weekday_express_by_string_list[len(weekday_express_by_string_list)-1]] - start_date.weekday())
            else:
                end_date = start_date + timedelta(days=28+WEEKDAY_CONVERT_TO_NUMBER_OR_STRING[weekday_express_by_string_list[j-1]] - start_date.weekday())

            one_month_schedule.append( {
                'start_date_time':str(start_date.month)+"-"+str(start_date.day)+"("+WEEKDAY_CONVERT_TO_NUMBER_OR_STRING[start_date.weekday()]+") " + str(start_time_express_by_string_list[j]),
                'start_date_time_unprocessed': str(start_date),
                'end_date_time':str(end_date.month)+"-"+str(end_date.day)+"("+WEEKDAY_CONVERT_TO_NUMBER_OR_STRING[end_date.weekday()]+") " + str(start_time_express_by_string_list[j]),
                'end_date_time_unprocessed': str(end_date)
            })

        for j in range( 0, current_weekday_position+1 ):
            if (today+timedelta_from_today).weekday() <= WEEKDAY_CONVERT_TO_NUMBER_OR_STRING[weekday_express_by_string_list[j]]:
                timedelta_from_today = timedelta(days=timedelta_from_today.days+WEEKDAY_CONVERT_TO_NUMBER_OR_STRING[weekday_express_by_string_list[j]]-(today+timedelta_from_today).weekday())
            else:
                timedelta_from_today = timedelta(days=7+timedelta_from_today.days+WEEKDAY_CONVERT_TO_NUMBER_OR_STRING[weekday_express_by_string_list[j]]-(today+timedelta_from_today).weekday())

            start_date = today+timedelta_from_today
            if j == 0:
                end_date = start_date + timedelta(days=21+WEEKDAY_CONVERT_TO_NUMBER_OR_STRING[weekday_express_by_string_list[len(weekday_express_by_string_list)-1]] - start_date.weekday())
            else:
                end_date = start_date + timedelta(days=28+WEEKDAY_CONVERT_TO_NUMBER_OR_STRING[weekday_express_by_string_list[j-1]] - start_date.weekday())

            one_month_schedule.append( {
                'start_date_time':str(start_date.month)+"-"+str(start_date.day)+"("+WEEKDAY_CONVERT_TO_NUMBER_OR_STRING[start_date.weekday()]+") " + str(start_time_express_by_string_list[j]),
                'start_date_time_unprocessed': str(start_date),
                'end_date_time':str(end_date.month)+"-"+str(end_date.day)+"("+WEEKDAY_CONVERT_TO_NUMBER_OR_STRING[end_date.weekday()]+") " + str(start_time_express_by_string_list[j]),
                'end_date_time_unprocessed': str(end_date)
            })

    classes_detail.update({
        'one_month_schedule':one_month_schedule
    })

    # print repr(classes)
    return _http_json_response(None, classes_detail )

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
        return HttpResponse( json.dumps( _make_json_response( True, None ) ), content_type="application/json" )

@csrf_exempt
def recommend_subcategory_view(request):
    sub_category_recommends = list ( SubCategoryRecommend.objects.values('image_url'))

    for sub_category_recommend in sub_category_recommends:
        sub_category_recommend['image_url'] = 'http://' + request.get_host() + sub_category_recommend['image_url']

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
            'count_of_month': classes_item.countOfMonth,
            'price_of_day': classes_item.priceOfDay,
            'original_price_of_month': classes_item.priceOfDay*classes_item.priceOfDay,
            'discount_price_of_month': classes_item.priceOfMonth,
            'image_url': 'http://' + request.get_host() + classes_item.company.thumbnail_image_url,
            'discount_rate': round(100 - classes_item.priceOfMonth*100.0/(classes_item.priceOfDay*classes_item.countOfMonth))
        })
        schedules = classes_item.get_schedules.filter(pk__in=schedule_pks).all()
        for schedule in schedules:
            classes_list_item_detail = classes_list_item.copy()

            # get weekday
            weekday_express_by_string_list = schedule.dayOfWeek.split(',')

            # get start time
            start_time_list = schedule.startTime.split(',')

            times = []
            for i in range(len(weekday_express_by_string_list)):
                times.append(weekday_express_by_string_list[i] + " : " + start_time_list[i])

            classes_list_item_detail.update({
                'times': times,
                'duration': schedule.duration.strftime("%H시간%M분").decode('utf-8'),
                'schedule_id': schedule.id
            })

            classes_list.append(classes_list_item_detail)

    return _http_json_response(None, classes_list)

@csrf_exempt
def nowtaking_view(request):
    purchases = Purchase.objects.get(class_end_datetime__gte=datetime.now())

    nowtaking_list = []

    for purchase in purchases:
        classes = purchase.classes
        schedule = purchase.schedule

        title = classes.title

        weekday_before_split_expressed_by_string = schedule.dayOfWeek
        weekday_list_expressed_by_string = weekday_before_split_expressed_by_string.split(',')
        start_time_before_split_expressed_by_string = schedule.startTime
        start_time_list_expressed_by_string = start_time_before_split_expressed_by_string.split(',')
        duration_expressed_by_string = schedule.duration
        duration_time = datetime.strptime(duration_expressed_by_string, '%H:%M:%S').time()

        time = ''

        if len(weekday_list_expressed_by_string) == len(start_time_list_expressed_by_string):
            for i in range(len(weekday_list_expressed_by_string)):
                if i != 0:
                    time += ', '
                weekday_expressed_by_korean = WEEKDAY_CONVERT_TO_KOREAN[weekday_list_expressed_by_string[i]]
                start_time = datetime.strptime(start_time_list_expressed_by_string[i], '%H:%M:%S').time()
                end_time = (datetime.combine( datetime.today(), start_time) + \
                          timedelta(hours=duration_time.hour, minutes=duration_time.minute)).time()

                time += weekday_expressed_by_korean + start_time.strftime(' %H:%M-') + end_time.strftime('%H:%M')

        else:
            pass

        start_datetime = purchase.class_start_datetime
        end_datetime = purchase.class_end_datetime
        current_state = purchase.state

        nowtaking_item = {
            'title': title,
            'time': time,
            'start_datetime': start_datetime.strftime("%Y-%m-%d") +
                              WEEKDAY_CONVERT_TO_KOREAN[WEEKDAY_CONVERT_TO_NUMBER_OR_STRING[start_datetime.strftime("%w")]],
            'end_datetime': end_datetime.strftime("%Y-%m-%d") +
                            WEEKDAY_CONVERT_TO_KOREAN[WEEKDAY_CONVERT_TO_NUMBER_OR_STRING[end_datetime.strftime("%w")]],
            'current_state': current_state
        }

        nowtaking_list.append(nowtaking_item)

    return _http_json_response(None, nowtaking_list)



def import_all_view(request):
    import_category_csv_file_view(request)
    import_sub_category_csv_file_view(request)
    import_company_csv_file_view(request)
    import_classes_csv_file_view(request)
    import_schedule_csv_file_view(request)
    import_sub_category_recommend_csv_file_view(request)

    return HttpResponse('success')

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

    return HttpResponse('success')


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

    return HttpResponse('success')


def import_company_csv_file_view(request):
    with open('./classes/resource/model/csv/company_model.csv', 'rb') as f:
        reader = csv.reader(f,  delimiter='|')
        is_first = True

        for row in reader:
            if is_first:
                is_first = False
                continue

            company, created = Company.objects.get_or_create(
                name=unicode(row[0], 'euc-kr'),
                phone_number=unicode(row[1], 'euc-kr'),
                location=unicode(row[2], 'euc-kr'),
                zone=unicode(row[3], 'euc-kr'),
                nearby_station=unicode(row[4], 'euc-kr'),
                facilitiesInformation=unicode(row[5], 'euc-kr'),
                thumbnail_image_url=unicode(row[6], 'euc-kr'))

            for i in range(7, len(row)):
                if len(row[i]) > 0:
                    CompanyImage.objects.get_or_create(
                        company=company,
                        image_url=unicode(row[i], 'euc-kr')
                    )

    return HttpResponse('success')


def import_classes_csv_file_view(request):
    with open('./classes/resource/model/csv/classes_model.csv', 'rb') as f:
        reader = csv.reader(f,  delimiter='|')
        is_first = True

        for row in reader:
            if is_first:
                is_first = False
                continue

            try:
                sub_category = SubCategory.objects.get(name=unicode(row[2], 'euc-kr'))
            except Exception, e:
                print unicode(row[2], 'euc-kr'), e

            try:
                company = Company.objects.get(name=unicode(row[3], 'euc-kr'))
            except Exception, e:
                print unicode(row[3], 'euc-kr'), e

            Classes.objects.get_or_create(
                title=unicode(row[0], 'euc-kr'),
                thumbnail_image_url=unicode(row[1], 'euc-kr'),
                subCategory=sub_category,
                company=company,
                description=unicode(row[4], 'euc-kr'),
                preparation=unicode(row[5], 'euc-kr'),
                personalOrGroup=unicode(row[6], 'euc-kr'),
                refundInformation=unicode(row[7], 'euc-kr'),
                priceOfDay=unicode(row[8], 'euc-kr'),
                countOfMonth=unicode(row[9], 'euc-kr'),
                priceOfMonth=unicode(row[10], 'euc-kr'),
                image_url=unicode(row[11], 'euc-kr'))

    return HttpResponse('success')

def import_schedule_csv_file_view(request):
    with open('./classes/resource/model/csv/schedule_model.csv', 'rb') as f:
        reader = csv.reader(f,  delimiter='|')
        is_first = True

        for row in reader:
            if is_first:
                is_first = False
                continue

            try:
                sub_category = SubCategory.objects.get(name=unicode(row[2], 'euc-kr'))
            except Exception, e:
                print unicode(row[2], 'euc-kr'), e

            try:
                company = Company.objects.get(name=unicode(row[3], 'euc-kr'))
            except Exception, e:
                print unicode(row[3], 'euc-kr'), e

            try:
                classes = Classes.objects.get(
                    title=unicode(row[0], 'euc-kr'),
                    thumbnail_image_url=unicode(row[1], 'euc-kr'),
                    subCategory=sub_category,
                    company=company,
                    description=unicode(row[4], 'euc-kr'),
                    preparation=unicode(row[5], 'euc-kr'),
                    personalOrGroup=unicode(row[6], 'euc-kr'),
                    refundInformation=unicode(row[7], 'euc-kr'),
                    priceOfDay=unicode(row[8], 'euc-kr'),
                    countOfMonth=unicode(row[9], 'euc-kr'),
                    priceOfMonth=unicode(row[10], 'euc-kr'),
                    image_url=unicode(row[11], 'euc-kr'))
            except Exception, e:
                logger.info(e)

            Schedule.objects.get_or_create(
                classes=classes,
                dayOfWeek=unicode(row[12], 'euc-kr'),
                startTime=unicode(row[13], 'euc-kr'),
                duration=unicode(row[14], 'euc-kr'))

    return HttpResponse('success')

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

# import csv
#
# def import_category_csv_file_view(request):
#     with open('./classes/resource/model/csv/category_model.csv', 'rb') as f:
#         reader = csv.reader(f,  delimiter='|')
#
#         headers = None
#         for row in reader:
#
#             if headers is None:
#                 headers = row
#             else:
#                 category = Category()
#                 for i in range(len(headers)):
#                     # category = Category(**{headers[i]: row[i]})
#                     setattr(category, headers[i], row[i])
#
#                 try:
#                     category.save()
#                 except:
#                     pass
#
#     return HttpResponse('success')
#
# def import_sub_category_csv_file_view(reqeust):
#     # subCategory = SubCategory(name='test',name_kor='테스트',description='ddd',image_url='http://test')
#     # ppp = Category.objects.filter(name='music').first().id
#     # print ppp
#     # subCategory.category.name = 'music'
#     # subCategory.save()
#
#     with open('./classes/resource/model/csv/sub_category_model.csv', 'rb') as f:
#         reader = csv.reader(f,  delimiter='|')
#
#         headers = None
#         for row in reader:
#
#             if headers is None:
#                 headers = row
#             else:
#                 sub_category = SubCategory()
#                 for i in range(len(headers)):
#                     if str(headers[i]).__contains__('__'):
#                         headers_list = str(headers[i]).split('__')
#                     setattr(sub_category, headers[i], unicode(row[i], 'euc-kr') )
#
#                 # print sub_category.category_name
#                 # print sub_category.name, sub_category
#
#                 try:
#                     sub_category.save()
#                 except Exception, e:
#                     print e
#
#     return HttpResponse('success')

# def category_csv_import():
#     category = Category(name='test')
#     category.save()