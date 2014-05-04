# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from classes.models import Classes, Schedule
import datetime


class ApiLog(models.Model):
    user_session_id = models.TextField(null=False, blank=True, default='')
    path_name = models.TextField(null=False, blank=True, default='')
    view_name = models.TextField(null=False, blank=True, default='')
    request_params = models.TextField(null=False, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now)

    def __unicode__(self):
        return 'ApiLog : %r' % self.user_session_id


class UserSession(models.Model):
    user = models.ForeignKey(User, related_name='get_sessions')
    user_session_id = models.TextField(null=False, blank=True, default='')

    class Meta:
        unique_together = ("user", "user_session_id")


class PaymentLog(models.Model):
    p_status = models.CharField(max_length=5, default='')
    p_tid = models.CharField(max_length=40, default='')
    p_type = models.CharField(max_length=10, default='') # ISP(신용카드 ISP), CARD(신용카드 안심클릭), HPMN(해피머니), CULTURE(문화상품권), MOBILE(휴대폰), VBANK(가상계좌), BANK(계좌이체)
    p_auth_dt = models.CharField(max_length=14, default='') # YYYYmmddHHmmss
    p_mid = models.CharField(max_length=10, default='')
    p_oid = models.CharField(max_length=100, default='')
    p_amt = models.CharField(max_length=8, default='')
    p_uname = models.CharField(max_length=30, default='')
    p_rmesg1 = models.CharField(max_length=500, default='')
    p_rmesg2 = models.CharField(max_length=500, default='')
    p_noti = models.CharField(max_length=1024, default='')
    p_fn_cd1 = models.CharField(max_length=4, default='')
    p_auth_no = models.CharField(max_length=30, default='')
    p_card_issuer_code = models.CharField(max_length=2, default='')
    p_card_num = models.TextField(default='')
    p_card_member_num = models.TextField(default='')
    p_card_purchase_code = models.TextField(default='')
    p_card_prtc_code = models.CharField(max_length=1, default='') # 부분취소가능 : 1, 부분취소불가능 : 0
    p_hpp_corp = models.CharField(max_length=3, default='')
    p_vact_num = models.CharField(max_length=20, default='') # 입금마감 일자 yyyymmdd
    p_vact_date = models.CharField(max_length=8, default='') # 입금마감 시간 hhmmss
    p_vact_time = models.CharField(max_length=6, default='')
    p_vact_name = models.TextField(default='')
    p_vact_bank_code = models.CharField(max_length=2, default='')


class Purchase(models.Model):
    payment_log = models.OneToOneField(PaymentLog, primary_key=True)
    user = models.ForeignKey(User, related_name='get_purchases')
    classes = models.ForeignKey(Classes, related_name='get_purchases')
    schedule = models.ForeignKey(Schedule, related_name='get_purchases')
    day_or_month = models.TextField(null=False, blank=True, default='month') # day | month
    class_start_date = models.TextField(default='')
    price = models.IntegerField(null=False, default=0)
    created = models.DateTimeField(null=False, auto_now=True)