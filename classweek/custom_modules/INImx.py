# -*- coding: utf-8 -*-

import logging
import requests
import urlparse

class INImx():

    #
    logger = None

    P_TID = None
    P_STATUS = None
    P_RMESG1 = None
    P_REQ_URL = None
    P_NOTI = None

    # 요청 구분 : 공통
    reqtype = None

    # 인증 및 승인요청
    inipayhome = None
    id_merchant = None
    status = None
    rmesg1 = None
    tid = None
    req_url = None
    noti = None

    # 클래스 내부 용
    m_serviceurl = None
    m_resultCode = None
    m_resultmsg = None
    m_resultprice = None
    m_pgAuthDate = None
    m_authCode = None
    m_cardQuota = None
    m_cardCode = None
    m_cardIssuerCode = None
    m_vacct = None
    m_vcdbank = None
    m_dtinput = None
    m_tminput = None
    m_nminput = None
    m_buyerName = None
    m_nextUrl = None
    m_notiUrl = None
    m_prtc = None

    # 결과 파싱용
    result_p_status = None
    result_p_tid = None
    result_p_type = None
    result_p_auth_dt = None
    result_p_mid = None
    result_p_oid = None
    result_p_amt = None
    result_p_uname = None
    result_p_rmesg1 = None
    result_p_rmesg2 = None
    result_p_noti = None
    result_p_fn_cd1 = None
    result_p_auth_no = None
    result_p_card_issuer_code = None
    result_p_card_num = None
    result_p_card_member_num = None
    result_p_card_purchase_code = None
    result_p_card_prtc_code = None
    result_p_hpp_corp_ = None
    result_p_vact_num = None
    result_p_vact_date = None
    result_p_vact_time = None
    result_p_vact_name = None
    result_p_vact_bank_code = None


    def __init__(self, request, request_name):

        self.logger = logging.getLogger(request_name)
        self.logger.debug('INImx def __init__(self, request, request_name):')

        self.P_TID = request.POST.get('P_TID', None)
        self.P_STATUS = request.POST.get('P_STATUS', None)
        self.P_RMESG1 = request.POST.get('P_RMESG1', None)
        self.P_REQ_URL = request.POST.get('P_REQ_URL', None)
        self.P_NOTI = request.POST.get('P_NOTI', None)

    # send request to req_url
    def start_action(self):

        self.logger.debug('INImx def start_action(self):')

        self.logger.debug('Start INImx_AUTH : ' + self.reqtype)
        self.logger.debug('INIPAYHOME : ' + self.inipayhome)
        self.logger.debug('P_MID : ' + self.id_merchant)
        self.logger.debug('P_STATUS : ' + self.status)
        self.logger.debug('P_RMESG1 : ' + self.rmesg1)
        self.logger.debug('P_TID : ' + self.tid)
        self.logger.debug('P_REQ_URL : ' + self.req_url)
        self.logger.debug('P_NOTI : ' + self.noti)
        self.logger.debug('AUTH Transaction End')

        if self.reqtype == "PAY":
            self.do_pay()

    def do_pay(self):
        params = {
            'P_MID': self.id_merchant,
            'P_TID': self.tid
        }
        response = requests.post(self.req_url, data=params)
        response.encoding = 'euc-kr'

        params_list = response.text.strip().split('&')
        params_dict = {}

        for params_item in params_list:
            params_item_split = params_item.split("=")
            params_item_key = params_item_split[0]
            params_item_value = params_item_split[1]
            params_dict[params_item_key]= params_item_value

        result_p_status = params_dict.get('P_STATUS', '')
        result_p_tid = params_dict.get('P_TID', '')
        result_p_type = params_dict.get('P_TYPE', '')
        result_p_auth_dt = params_dict.get('P_AUTH_DT', '')
        result_p_mid = params_dict.get('P_MID', '')
        result_p_oid = params_dict.get('P_OID', '')
        result_p_amt = params_dict.get('P_AMT', '')
        result_p_uname = params_dict.get('P_UNAME', '')
        result_p_rmesg1 = params_dict.get('P_RMESG1', '')
        result_p_rmesg2 = params_dict.get('P_RMESG2', '')
        result_p_noti = params_dict.get('P_NOTI', '')
        result_p_fn_cd1 = params_dict.get('P_FN_CD1', '')
        result_p_auth_no = params_dict.get('P_AUTH_NO', '')
        result_p_card_issuer_code = params_dict.get('P_CARD_ISSUER_CODE', '')
        result_p_card_num = params_dict.get('P_CARD_NUM', '')
        result_p_card_member_num = params_dict.get('P_CARD_MEMBER_NUM', '')
        result_p_card_purchase_code = params_dict.get('P_CARD_PURCHASE_CODE', '')
        result_p_card_prtc_code = params_dict.get('P_CARD_PRTC_CODE', '')
        result_p_hpp_corp = params_dict.get('P_HPP_CORP', '')
        result_p_vact_num = params_dict.get('P_VACT_NUM', '')
        result_p_vact_date = params_dict.get('P_VACT_DATE', '')
        result_p_vact_time = params_dict.get('P_VACT_TIME', '')
        result_p_vact_name = params_dict.get('P_VACT_NAME', '')
        result_p_vact_bank_code = params_dict.get('P_VACT_CODE', '')

        self.logger.debug('P_STATUS : ' + result_p_status)
        self.logger.debug('P_TID : ' + result_p_tid)
        self.logger.debug('P_TYPE : ' + result_p_type)
        self.logger.debug('P_AUTH_DT : ' + result_p_auth_dt)
        self.logger.debug('P_MID : ' + result_p_mid)
        self.logger.debug('P_OID : ' + result_p_oid)
        self.logger.debug('P_AMT : ' + result_p_amt)
        self.logger.debug('P_UNAME : ' + result_p_uname)
        self.logger.debug('P_RMESG1 : ' + result_p_rmesg1)
        self.logger.debug('P_RMESG2 : ' + result_p_rmesg2)
        self.logger.debug('P_NOTI : ' + result_p_noti)
        self.logger.debug('P_FN_CD1 : ' + result_p_fn_cd1)
        self.logger.debug('P_AUTH_NO : ' + result_p_auth_no)
        self.logger.debug('P_CARD_ISSUER_CODE : ' + result_p_card_issuer_code)
        self.logger.debug('P_CARD_NUM : ' + result_p_card_num)
        self.logger.debug('P_CARD_MEMBER_NUM : ' + result_p_card_member_num)
        self.logger.debug('P_CARD_PURCHASE_CODE : ' + result_p_card_purchase_code)
        self.logger.debug('P_CARD_PRTC_CODE : ' + result_p_card_prtc_code)
        self.logger.debug('P_HPP_CORP : ' + result_p_hpp_corp)
        self.logger.debug('P_VACT_NUM : ' + result_p_vact_num)
        self.logger.debug('P_VACT_DATE : ' + result_p_vact_date)
        self.logger.debug('P_VACT_TIME : ' + result_p_vact_time)
        self.logger.debug('P_VACT_NAME : ' + result_p_vact_name)
        self.logger.debug('P_VACT_CODE : ' + result_p_vact_bank_code)