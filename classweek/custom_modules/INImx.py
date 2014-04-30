# -*- coding: utf-8 -*-

import logging
import httplib, urllib

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

    # 클래스 내부 용
    m_serviceurl = None
    m_resultCode = None
    m_resultmsg = None
    noti = None
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


    def __init__(self, request, request_name):

        self.logger = logging.getLogger(request_name)
        self.logger.debug('INImx def __init__(self, request, request_name):')

        self.P_TID = request.POST.get('P_TID', None)
        self.P_STATUS = request.POST.get('P_TID', None)
        self.logger.debug('status = ' + self.P_STATUS)
        self.P_RMESG1 = request.POST.get('P_RMESG1', None)
        self.P_REQ_URL = request.POST.get('P_REQ_URL', None)
        self.P_NOTI = request.POST.get('P_NOTE', None)
        pass

    def start_action(self):

        self.logger.debug('INImx def start_action(self):')

        self.logger.debug('Start INImx_AUTH' + self.reqtype.VERSION)
        self.logger.debug('INIPAYHOME' + self.inipayhome)
        self.logger.debug('P_MID' + self.id_merchant)
        self.logger.debug('P_STATUS' + self.status)
        self.logger.debug('P_RMESG1' + self.rmesg1)
        self.logger.debug('P_TID' + self.tid)
        self.logger.debug('P_REQ_URL' + self.req_url)
        self.logger.debug('P_NOTI' + self.noti)
        self.logger.debug('AUTH Transaction End')

        if self.reqtype == "PAY":
            self.do_pay()

    def do_pay(self):
        params = urllib.urlencode({'P_MID': self.id_merchant, 'P_TID': self.tid})
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
        conn = httplib.HTTPConnection("hostname:post")
        conn.request("POST","/index.html",params, headers)
        response = conn.getresponse()
        self.logger.debug( response )
        self.logger.debug( dir(response) )
        pass

#     function startAction()
# 	{
# 		$this->printLog("Start INImx_AUTH ".$this->reqtype.VERSION);
# 		$this->printLog("INIPAYHOME:".$this->inipayhome);
# 		$this->printLog("P_MID:".$this->id_merchant);
# 		$this->printLog("P_STATUS:".$this->status);
# 		$this->printLog("P_RMESG1:".$this->rmesg1);
# 		$this->printLog("P_TID:".$this->tid);
# 		$this->printLog("P_REQ_URL:".$this->req_url);
# 		$this->printLog("P_NOTI:".$this->noti);
# 		$this->printLog("AUTH Transaction End");
#
# 		switch($this->reqtype)
# 		{
# 			case("PAY"):
# 				$this->doPay();
# 			break;
#
# 		}
# //		$this->printLog("End INImx ".$this->reqtype.VERSION);
# 	}