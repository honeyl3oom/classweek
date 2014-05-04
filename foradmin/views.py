# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from classweek.custom_modules.INImx import INImx
from django.templatetags.static import static
from foradmin.models import Purchase, PaymentLog
from classes.models import Classes, Schedule

import json

import logging

logger = logging.getLogger(__name__)

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
def payment_next_test_view(request):

    logger.debug('def payment_next_test_view(request):')
    logger.debug(request.GET)
    logger.debug(request.POST)

    inimx = INImx(request, __name__)

    inimx.reqtype = "PAY"
    inimx.inipayhome = "/home/ts/INIpay50/" # 로그기록 경로 (이 위치의 하위폴더에 log폴더 생성 후 log폴더에 대해 777 권한 설정)
    inimx.id_merchant = inimx.P_TID[10:20]
    inimx.status = inimx.P_STATUS
    inimx.rmesg1 = inimx.P_RMESG1
    inimx.tid = inimx.P_TID
    inimx.req_url = inimx.P_REQ_URL
    inimx.noti = inimx.P_NOTI

    if inimx.status == "00":
        inimx.start_action()


    return HttpResponse('payment_next_test_view')

@csrf_exempt
def payment_noti_test_view(request):

    logger.debug('def payment_noti_test_view(request):')
    logger.debug(request.GET)
    logger.debug(request.POST)

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

        payment_log = PaymentLog.objects.create(
            p_status=unicode(p_status, 'euc-kr'),
            p_tid=unicode(p_tid, 'euc-kr'),
            p_type=unicode(p_type, 'euc-kr'),
            p_auth_dt=unicode(p_auth_dt, 'euc-kr'),
            p_mid=unicode(p_mid, 'euc-kr'),
            p_oid=unicode(p_oid, 'euc-kr'),
            p_amt=unicode(p_amt, 'euc-kr'),
            p_uname=unicode(p_uname, 'euc-kr'),
            p_rmesg1=unicode(p_rmesg1, 'euc-kr'),
            p_rmesg2=unicode(p_rmesg2, 'euc-kr'),
            p_noti=unicode(p_noti, 'euc-kr'),
            p_fn_cd1=unicode(p_fn_cd1, 'euc-kr'),
            p_auth_no=unicode(p_auth_no, 'euc-kr'),
            p_card_issuer_code=unicode(p_card_issuer_code, 'euc-kr'),
            p_card_num=unicode(p_card_num, 'euc-kr'),
            p_card_member_num=unicode(p_card_member_num, 'euc-kr'),
            p_card_purchase_code=unicode(p_card_purchase_code, 'euc-kr'),
            p_card_prtc_code=unicode(p_card_prtc_code, 'euc-kr'),
            p_hpp_corp=unicode(p_hpp_corp, 'euc-kr'),
            p_vact_num=unicode(p_vact_num, 'euc-kr'),
            p_vact_date=unicode(p_vact_date, 'euc-kr'),
            p_vact_time=unicode(p_vact_time, 'euc-kr'),
            p_vact_name=unicode(p_vact_name, 'euc-kr'),
            p_vact_bank_code=unicode(p_vact_bank_code, 'euc-kr')
        )

        if request.user.is_authenticated():
            payment_item_info_json = json.loads(p_noti)

            classes_id = payment_item_info_json.get('classes_id', None)
            classes = Classes.objects.get(id=classes_id) if classes_id is not None else None

            schedule_id = payment_item_info_json.get('schedule_id', None)
            schedule = Schedule.objects.get(id=schedule_id) if schedule_id is not None else None

            if classes is None or schedule is None:
                logger.error('payment item info is not correct')

            Purchase(
                payment_log=payment_log,
                user=request.user,
                classes=classes,
                schedule=schedule,
                day_or_month=payment_item_info_json.get('day_or_month', ''),
                class_start_date=payment_item_info_json.get('class_start_date', ''),
                price=payment_item_info_json.get('price', 0)
            )
        else:
            logger.error('not authenticated user payment')
        
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


    return HttpResponse('def payment_noti_test_view(request):')

@csrf_exempt
def payment_return_test_view(request):

    logger.debug('def payment_return_test_view(request):')
    logger.debug( request.GET )
    logger.debug( request.POST )

    return HttpResponse('payment_return_test_view')