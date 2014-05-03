# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from classweek.custom_modules.INImx import INImx
from django.templatetags.static import static
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
    logger.debug( request.GET )
    logger.debug( request.POST )

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
    logger.debug(request.META.REMOTE_ADDR)

    if request.META.REMOTE_ADDR in ("118.129.210.25", "211.219.96.165", "118.129.210.24", "192.168.187.140", "172.20.22.40"):
        result_p_status = request.POST.get('P_STATUS', '')
        result_p_tid = request.POST.get('P_TID', '')
        result_p_type = request.POST.get('P_TYPE', '')
        result_p_auth_dt = request.POST.get('P_AUTH_DT', '')
        result_p_mid = request.POST.get('P_MID', '')
        result_p_oid = request.POST.get('P_OID', '')
        result_p_amt = request.POST.get('P_AMT', '')
        result_p_uname = request.POST.get('P_UNAME', '')
        result_p_rmesg1 = request.POST.get('P_RMESG1', '')
        result_p_rmesg2 = request.POST.get('P_RMESG2', '')
        result_p_noti = request.POST.get('P_NOTI', '')
        result_p_fn_cd1 = request.POST.get('P_FN_CD1', '')
        result_p_auth_no = request.POST.get('P_AUTH_NO', '')
        result_p_card_issuer_code = request.POST.get('P_CARD_ISSUER_CODE', '')
        result_p_card_num = request.POST.get('P_CARD_NUM', '')
        result_p_card_member_num = request.POST.get('P_CARD_MEMBER_NUM', '')
        result_p_card_purchase_code = request.POST.get('P_CARD_PURCHASE_CODE', '')
        result_p_card_prtc_code = request.POST.get('P_CARD_PRTC_CODE', '')
        result_p_hpp_corp = request.POST.get('P_HPP_CORP', '')
        result_p_vact_num = request.POST.get('P_VACT_NUM', '')
        result_p_vact_date = request.POST.get('P_VACT_DATE', '')
        result_p_vact_time = request.POST.get('P_VACT_TIME', '')
        result_p_vact_name = request.POST.get('P_VACT_NAME', '')
        result_p_vact_bank_code = request.POST.get('P_VACT_CODE', '')
        
        logger.debug('P_STATUS : ' + result_p_status)
        logger.debug('P_TID : ' + result_p_tid)
        logger.debug('P_TYPE : ' + result_p_type)
        logger.debug('P_AUTH_DT : ' + result_p_auth_dt)
        logger.debug('P_MID : ' + result_p_mid)
        logger.debug('P_OID : ' + result_p_oid)
        logger.debug('P_AMT : ' + result_p_amt)
        logger.debug('P_UNAME : ' + result_p_uname)
        logger.debug('P_RMESG1 : ' + result_p_rmesg1)
        logger.debug('P_RMESG2 : ' + result_p_rmesg2)
        logger.debug('P_NOTI : ' + result_p_noti)
        logger.debug('P_FN_CD1 : ' + result_p_fn_cd1)
        logger.debug('P_AUTH_NO : ' + result_p_auth_no)
        logger.debug('P_CARD_ISSUER_CODE : ' + result_p_card_issuer_code)
        logger.debug('P_CARD_NUM : ' + result_p_card_num)
        logger.debug('P_CARD_MEMBER_NUM : ' + result_p_card_member_num)
        logger.debug('P_CARD_PURCHASE_CODE : ' + result_p_card_purchase_code)
        logger.debug('P_CARD_PRTC_CODE : ' + result_p_card_prtc_code)
        logger.debug('P_HPP_CORP : ' + result_p_hpp_corp)
        logger.debug('P_VACT_NUM : ' + result_p_vact_num)
        logger.debug('P_VACT_DATE : ' + result_p_vact_date)
        logger.debug('P_VACT_TIME : ' + result_p_vact_time)
        logger.debug('P_VACT_NAME : ' + result_p_vact_name)
        logger.debug('P_VACT_CODE : ' + result_p_vact_bank_code)


    return HttpResponse('def payment_noti_test_view(request):')

@csrf_exempt
def payment_return_test_view(request):

    logger.debug('def payment_return_test_view(request):')
    logger.debug( request.GET )
    logger.debug( request.POST )

    return HttpResponse('payment_return_test_view')