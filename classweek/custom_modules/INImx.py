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
        response = requests.post( self.req_url, data=params)
        response.encoding='euc-kr'
        # response_body = repr(response.text).decode('utf-8').encode('utf-8')
        # self.logger.debug(response_body)
        # self.logger.debug('한글잘나오나')
        # self.logger.debug(response.text)
        # response_body = repr(response.text)
        # self.logger.debug(response.encoding)
        # # response_body = unicode(response_body, 'iso-8859-1').encode('utf-8')
        # response_body = response_body.decode('iso-8859-1')
        # response_body = response_body.encode('euc-kr')
        # response_body = response_body.strip()
        # self.logger.debug(response_body)
        # self.logger.debug(response_body)
        # self.logger.debug(response_body.strip())
        # self.logger.debug(unicode(response_body.strip(), 'euc-kr'))
        # self.logger.debug(unicode(response_body.strip(), 'utf-8'))
        # self.logger.debug(response_body.strip().encode('euc-kr'))
        # self.logger.debug(response_body.strip().encode('utf-8'))

        params_list = response.text.strip().split('&')
        params_dict = {}

        for params_item in params_list:
            params_item_split = params_item.split("=")
            params_item_key = params_item_split[0]
            params_item_value = params_item_split[1]
            params_dict[params_item_key]= params_item_value

        result_p_status = params_dict.get('P_STATUS', None)
        self.logger.debug(result_p_status)
        # result_p_tid = None
        # result_p_type = None
        # result_p_auth_dt = None
        # result_p_mid = None
        # result_p_oid = None
        # result_p_amt = None
        # result_p_uname = None
        # result_p_rmesg1 = None
        # result_p_rmesg2 = None
        # result_p_noti = None
        # result_p_fn_cd1 = None
        # result_p_auth_no = None
        # result_p_card_issuer_code = None
        # result_p_card_num = None
        # result_p_card_member_num = None
        # result_p_card_purchase_code = None
        # result_p_card_prtc_code = None
        # result_p_hpp_corp_ = None
        # result_p_vact_num = None
        # result_p_vact_date = None
        # result_p_vact_time = None
        # result_p_vact_name = None
        # result_p_vact_bank_code = None

        self.logger.debug(params_dict)
        #
        #
        #
        # params_dict = urlparse.parse_qsl(response.text.strip())[0]
        # self.logger.debug(params_dict)
        # self.logger.debug(params_dict.get('P_STATUS', 'status is none'))
        # params_dict = {key.encode('utf-8'): value.encode('utf-8') for key, value in params_dict}
        # self.logger.debug(params_dict)
        # print params_dict.get('P_STATUS', 'status is none')

        # params_dict = urlparse.parse_qsl(response.text)
        # self.logger.debug(params_dict)
        #
        # params_dict = urlparse.parse_qsl(response.text)
        # params_dict = {key.encode('utf-8'): value.encode('utf-8') for key, value in params_dict}
        # self.logger.debug(params_dict)
        #
        #
        # response.encode = 'utf-8'
        #
        # params_dict = urlparse.parse_qsl(response.text)
        # self.logger.debug(params_dict)
        #
        # params_dict = {key.encode('utf-8'): value.encode('utf-8') for key, value in params_dict}
        # self.logger.debug(params_dict)
        #
        # params_dict = urlparse.parse_qsl(response.text)
        # params_dict = {key.encode('euc-kr'): value.encode('euc-kr') for key, value in params_dict}
        # self.logger.debug(params_dict)

        # response_data = urllib.urlopen(self.req_url, params).read()
        # self.logger.debug(response_data)
        # self.logger.debug(dir(response_data))
        # conn = httplib.HTTPConnection("hostname:post")
        # conn.request("POST", "/index.html", params, headers)
        # response = conn.getresponse()
        # self.logger.debug(response)
        # self.logger.debug(dir(response))