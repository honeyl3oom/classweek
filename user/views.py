# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

from forcompany.forms import CompanyInfoForm

def sign_up(request):
    response_data = {}
    response_data['result'] = 'success'
    response_data['message'] = 'sign up success'
    return HttpResponse( json.dumps(response_data), content_type="application/json")
