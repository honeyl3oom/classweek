# -*- coding: utf-8 -*-

class INImx():

    P_TID = None

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


    def __init__(self, request ):
        self.P_TID = request.POST.get('P_TID', None )
        pass

    def start_action(self):
        if self.reqtype == "PAY":
            self.do_pay()

    def do_pay(self):
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