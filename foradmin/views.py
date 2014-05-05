# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from foradmin.models import Purchase, PaymentLog
from classes.models import Classes, Schedule
from classweek.const import INICIS_MARKET_ID
import requests

import json

import logging

logger = logging.getLogger(__name__)


# P_MID, P_AMT, P_UNAME, P_NOTI,
# P_NEXT_URL, P_NOTI_URL, P_RETURN_URL, P_GOODS
@csrf_exempt
def before_payment_view(request):

    classes_id = request.POST.get('classes_id', None)
    schedule_id = request.POST.get('schedule_id', None)
    day_or_month = request.POST.get('day_or_month', None)
    class_start_date = request.POST.get('class_start_date', None)

    if None in (classes_id, schedule_id, day_or_month, class_start_date):
        return HttpResponse('error')

    print request.user
    print dir(request.user)

    if not(request.user.is_authenticated()) or not(hasattr(request.user, 'profile')):
        return HttpResponse('error')

    classes = Classes.objects.get(id=classes_id)
    P_MID = INICIS_MARKET_ID
    P_AMT = classes.priceOfMonth if day_or_month == 'month' else classes.priceOfDay
    P_UNAME = request.user.profile.name
    P_NOTI = json.dumps({
        'username': request.user.profile.name,
        'classes_id': classes_id,
        'schedule_id': schedule_id,
        'day_or_month': day_or_month,
        'class_start_date': class_start_date,
        'price': P_AMT
    })
    P_NEXT_URL = request.build_absolute_uri(reverse('payment_next', args=[]))
    P_NOTI_URL = request.build_absolute_uri(reverse('payment_noti', args=[]))
    P_RETURN_URL = request.build_absolute_uri(reverse('payment_return', args=[]))
    P_GOODS = 'blackpigstudio'+","+str(classes_id)+","+str(schedule_id)

    return HttpResponse(json.dumps(
        {
            'data': {
                'P_MID': P_MID,
                'P_AMT': P_AMT,
                'P_UNAME': P_UNAME,
                'P_NOTI': P_NOTI,
                'P_NEXT_URL': P_NEXT_URL,
                'P_NOTI_URL': P_NOTI_URL,
                'P_RETURN_URL': P_RETURN_URL,
                'P_GOODS': P_GOODS},
            'error_code': 0,
            'error_message': None,
            'result': 'success'
        }, ensure_ascii=False), content_type='"application/json; charset=utf-8"')

def payment_startweb_test_view(request):

    logger.debug("def payment_startweb_test_view(request):")
    # logger.debug("\xbc\xad\xba\xf1\xbd\xba".decode('EUC-KR').encode('UTF-8'))
    # logger.debug(u'\uc11c\ube44\uc2a4 \uc0ac\uc6a9\ubd88\uac00 \uac00\ub9f9\uc810')

    payment_next_url = request.build_absolute_uri(reverse('payment_next_test', args=[]))
    payment_return_url = request.build_absolute_uri(reverse('payment_return_test', args=[]))
    payment_noti_url = request.build_absolute_uri(reverse('payment_noti_test', args=[]))
    return render(request, 'payment_startweb_test.html',
                  {'payment_next_url': payment_next_url,
                   'payment_return_url': payment_return_url,
                   'payment_noti_url': payment_noti_url})

@csrf_exempt
def payment_next_view(request):

    logger.debug('def payment_next_test_view(request):')
    logger.debug(request.GET)
    logger.debug(request.POST)

    next_p_status = request.POST.get('P_STATUS', None)

    if next_p_status == "00":
        next_p_tid = request.POST.get('P_TID', None)
        params = {
            'P_MID': next_p_tid[10:20],
            'P_TID': next_p_tid
        }


        # send request and recive response
        next_req_url = request.POST.get('P_REQ_URL', None)
        response = requests.post(next_req_url, data=params )
        response.encoding = 'euc-kr'

        # parsing response data
        params_list = response.text.strip().split('&')
        params_dict = {}
        for params_item in params_list:
            params_item_split = params_item.split("=")
            params_item_key = params_item_split[0]
            params_item_value = params_item_split[1]
            params_dict[params_item_key]= params_item_value

        p_status = params_dict.get('P_STATUS', '')
        p_tid = params_dict.get('P_TID', '')
        p_type = params_dict.get('P_TYPE', '')
        p_auth_dt = params_dict.get('P_AUTH_DT', '')
        p_mid = params_dict.get('P_MID', '')
        p_oid = params_dict.get('P_OID', '')
        p_amt = params_dict.get('P_AMT', '')
        p_uname = params_dict.get('P_UNAME', '')
        p_rmesg1 = params_dict.get('P_RMESG1', '')
        p_rmesg2 = params_dict.get('P_RMESG2', '')
        p_noti = params_dict.get('P_NOTI', '')
        p_fn_cd1 = params_dict.get('P_FN_CD1', '')
        p_auth_no = params_dict.get('P_AUTH_NO', '')
        p_card_issuer_code = params_dict.get('P_CARD_ISSUER_CODE', '')
        p_card_num = params_dict.get('P_CARD_NUM', '')
        p_card_member_num = params_dict.get('P_CARD_MEMBER_NUM', '')
        p_card_purchase_code = params_dict.get('P_CARD_PURCHASE_CODE', '')
        p_card_prtc_code = params_dict.get('P_CARD_PRTC_CODE', '')
        p_hpp_corp = params_dict.get('P_HPP_CORP', '')
        p_vact_num = params_dict.get('P_VACT_NUM', '')
        p_vact_date = params_dict.get('P_VACT_DATE', '')
        p_vact_time = params_dict.get('P_VACT_TIME', '')
        p_vact_name = params_dict.get('P_VACT_NAME', '')
        p_vact_bank_code = params_dict.get('P_VACT_BANK_CODE', '')

        logger.debug('P_STATUS : ' + p_status)
        logger.debug('P_TID : ' + p_tid)
        logger.debug('P_TYPE : ' + p_type)
        logger.debug('P_AUTH_DT : ' + p_auth_dt)
        logger.debug('P_MID : ' + p_mid)
        logger.debug('P_OID : ' + p_oid)
        logger.debug('P_AMT : ' + p_amt)
        logger.debug('P_UNAME : ' + p_uname)
        logger.debug('P_RMESG1 : ' + p_rmesg1)
        logger.debug('P_RMESG2 : ' + p_rmesg2)
        logger.debug('P_NOTI : ' + p_noti)
        logger.debug('P_FN_CD1 : ' + p_fn_cd1)
        logger.debug('P_AUTH_NO : ' + p_auth_no)
        logger.debug('P_CARD_ISSUER_CODE : ' + p_card_issuer_code)
        logger.debug('P_CARD_NUM : ' + p_card_num)
        logger.debug('P_CARD_MEMBER_NUM : ' + p_card_member_num)
        logger.debug('P_CARD_PURCHASE_CODE : ' + p_card_purchase_code)
        logger.debug('P_CARD_PRTC_CODE : ' + p_card_prtc_code)
        logger.debug('P_HPP_CORP : ' + p_hpp_corp)
        logger.debug('P_VACT_NUM : ' + p_vact_num)
        logger.debug('P_VACT_DATE : ' + p_vact_date)
        logger.debug('P_VACT_TIME : ' + p_vact_time)
        logger.debug('P_VACT_NAME : ' + p_vact_name)
        logger.debug('P_VACT_BANK_CODE : ' + p_vact_bank_code)

        try:
            payment_log = PaymentLog.objects.create(
                p_status=p_status,
                p_tid=p_tid,
                p_type=p_type,
                p_auth_dt=p_auth_dt,
                p_mid=p_mid,
                p_oid=p_oid,
                p_amt=p_amt,
                p_uname=p_uname,
                p_rmesg1=p_rmesg1,
                p_rmesg2=p_rmesg2,
                p_noti=p_noti,
                p_fn_cd1=p_fn_cd1,
                p_auth_no=p_auth_no,
                p_card_issuer_code=p_card_issuer_code,
                p_card_num=p_card_num,
                p_card_member_num=p_card_member_num,
                p_card_purchase_code=p_card_purchase_code,
                p_card_prtc_code=p_card_prtc_code,
                p_hpp_corp=p_hpp_corp,
                p_vact_num=p_vact_num,
                p_vact_date=p_vact_date,
                p_vact_time=p_vact_time,
                p_vact_name=p_vact_name,
                p_vact_bank_code=p_vact_bank_code
            )
        except Exception, e:
            logger.error(e)

        payment_item_info_json = json.loads(p_noti)

        username = payment_item_info_json.get('username', None)
        user = User.objects.get(username=username) if username is not None else None

        classes_id = payment_item_info_json.get('classes_id', None)
        classes = Classes.objects.get(id=classes_id) if classes_id is not None else None

        schedule_id = payment_item_info_json.get('schedule_id', None)
        schedule = Schedule.objects.get(id=schedule_id) if schedule_id is not None else None

        if user is None:
            logger.error('not authenticated user payment')
        elif classes is None or schedule is None:
            logger.error('payment item info is not correct')
        else:
            purchase = Purchase.objects.create(
                payment_log=payment_log,
                user=request.user,
                classes=classes,
                schedule=schedule,
                day_or_month=payment_item_info_json.get('day_or_month', ''),
                class_start_date=payment_item_info_json.get('class_start_date', ''),
                price=payment_item_info_json.get('price', 0)
            )

    return HttpResponse('payment_next_test_view')

@csrf_exempt
def payment_noti_view(request):

    logger.debug('def payment_noti_test_view(request):')
    logger.debug(request.GET)
    logger.debug(request.POST)
    logger.debug(request.META.get('REMOTE_ADDR'))

    if request.META.get('REMOTE_ADDR') in ("118.129.210.25", "211.219.96.165", "118.129.210.24", "192.168.187.140", "172.20.22.40"):

        p_status = request.POST.get('P_STATUS', '')
        p_tid = request.POST.get('P_TID', '')
        p_type = request.POST.get('P_TYPE', '')
        p_auth_dt = request.POST.get('P_AUTH_DT', '')
        p_mid = request.POST.get('P_MID', '')
        p_oid = request.POST.get('P_OID', '')
        p_amt = request.POST.get('P_AMT', '')
        p_uname = request.POST.get('P_UNAME', '')
        p_rmesg1 = request.POST.get('P_RMESG1', '')
        p_rmesg2 = request.POST.get('P_RMESG2', '')
        p_noti = request.POST.get('P_NOTI', '')
        p_fn_cd1 = request.POST.get('P_FN_CD1', '')
        p_auth_no = request.POST.get('P_AUTH_NO', '')
        p_card_issuer_code = request.POST.get('P_CARD_ISSUER_CODE', '')
        p_card_num = request.POST.get('P_CARD_NUM', '')
        p_card_member_num = request.POST.get('P_CARD_MEMBER_NUM', '')
        p_card_purchase_code = request.POST.get('P_CARD_PURCHASE_CODE', '')
        p_card_prtc_code = request.POST.get('P_CARD_PRTC_CODE', '')
        p_hpp_corp = request.POST.get('P_HPP_CORP', '')
        p_vact_num = request.POST.get('P_VACT_NUM', '')
        p_vact_date = request.POST.get('P_VACT_DATE', '')
        p_vact_time = request.POST.get('P_VACT_TIME', '')
        p_vact_name = request.POST.get('P_VACT_NAME', '')
        p_vact_bank_code = request.POST.get('P_VACT_BANK_CODE', '')

        logger.debug('P_STATUS : ' + p_status)
        logger.debug('P_TID : ' + p_tid)
        logger.debug('P_TYPE : ' + p_type)
        logger.debug('P_AUTH_DT : ' + p_auth_dt)
        logger.debug('P_MID : ' + p_mid)
        logger.debug('P_OID : ' + p_oid)
        logger.debug('P_AMT : ' + p_amt)
        logger.debug('P_UNAME : ' + p_uname)
        logger.debug('P_RMESG1 : ' + p_rmesg1)
        logger.debug('P_RMESG2 : ' + p_rmesg2)
        logger.debug('P_NOTI : ' + p_noti)
        logger.debug('P_FN_CD1 : ' + p_fn_cd1)
        logger.debug('P_AUTH_NO : ' + p_auth_no)
        logger.debug('P_CARD_ISSUER_CODE : ' + p_card_issuer_code)
        logger.debug('P_CARD_NUM : ' + p_card_num)
        logger.debug('P_CARD_MEMBER_NUM : ' + p_card_member_num)
        logger.debug('P_CARD_PURCHASE_CODE : ' + p_card_purchase_code)
        logger.debug('P_CARD_PRTC_CODE : ' + p_card_prtc_code)
        logger.debug('P_HPP_CORP : ' + p_hpp_corp)
        logger.debug('P_VACT_NUM : ' + p_vact_num)
        logger.debug('P_VACT_DATE : ' + p_vact_date)
        logger.debug('P_VACT_TIME : ' + p_vact_time)
        logger.debug('P_VACT_NAME : ' + p_vact_name)
        logger.debug('P_VACT_BANK_CODE : ' + p_vact_bank_code)

        try:
            payment_log = PaymentLog.objects.create(
                p_status=p_status,
                p_tid=p_tid,
                p_type=p_type,
                p_auth_dt=p_auth_dt,
                p_mid=p_mid,
                p_oid=p_oid,
                p_amt=p_amt,
                p_uname=p_uname,
                p_rmesg1=p_rmesg1,
                p_rmesg2=p_rmesg2,
                p_noti=p_noti,
                p_fn_cd1=p_fn_cd1,
                p_auth_no=p_auth_no,
                p_card_issuer_code=p_card_issuer_code,
                p_card_num=p_card_num,
                p_card_member_num=p_card_member_num,
                p_card_purchase_code=p_card_purchase_code,
                p_card_prtc_code=p_card_prtc_code,
                p_hpp_corp=p_hpp_corp,
                p_vact_num=p_vact_num,
                p_vact_date=p_vact_date,
                p_vact_time=p_vact_time,
                p_vact_name=p_vact_name,
                p_vact_bank_code=p_vact_bank_code
            )
        except Exception, e:
            logger.error(e)

        payment_item_info_json = json.loads(p_noti)

        username = payment_item_info_json.get('username', None)
        user = User.objects.get(username=username) if username is not None else None

        classes_id = payment_item_info_json.get('classes_id', None)
        classes = Classes.objects.get(id=classes_id) if classes_id is not None else None

        schedule_id = payment_item_info_json.get('schedule_id', None)
        schedule = Schedule.objects.get(id=schedule_id) if schedule_id is not None else None

        if user is None:
            logger.error('not authenticated user payment')
        elif classes is None or schedule is None:
            logger.error('payment item info is not correct')
        else:
            purchase = Purchase.objects.create(
                payment_log=payment_log,
                user=request.user,
                classes=classes,
                schedule=schedule,
                day_or_month=payment_item_info_json.get('day_or_month', ''),
                class_start_date=payment_item_info_json.get('class_start_date', ''),
                price=payment_item_info_json.get('price', 0)
            )



    return HttpResponse('def payment_noti_test_view(request):')

@csrf_exempt
def payment_return_view(request):

    logger.debug('def payment_return_test_view(request):')
    logger.debug( request.GET )
    logger.debug( request.POST )

    return HttpResponse('payment_return_test_view')