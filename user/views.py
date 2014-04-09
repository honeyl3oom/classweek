# -*- coding: utf-8 -*-
import json
from django.views.decorators.csrf import csrf_exempt

from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from forcompany.forms import CompanyInfoForm

# response_data = {}
# response_data['result'] = 'success'
# response_data['message'] = 'registration success'
# return HttpResponse( json.dumps(response_data), content_type="application/json")

RESPONSE_STR_SUCCESS = 'success'
RESPONSE_STR_FAIL = 'fail'

ERROR_PASSWORD_CONFIRM_NOT_IDENTICAL = 'password confirm not identical'

# input : username, email, password
# @require_http_methods(["GET", "POST"])

def _makeJsonResponse( isSuccess, error_message ):
    data = {}
    if isSuccess:
        data['result'] = RESPONSE_STR_SUCCESS
    else:
        data['result'] = RESPONSE_STR_FAIL
    data['error_message'] = error_message
    return data

def _login( request, email, password ):

    error = None

    user = authenticate( username=email, password=password)
    if user is not None:
        if user.is_active:
            login( request, user )
        else:
            error = 'not actived'
    else:
        error = 'authenticate fail'

    return error

def _registration( email, password, password_confirm ):
    error = None
    if password == password_confirm:
        try:
            user = User.objects.create_user( email, email, password )
        except Exception, e:
            error = repr(e)
    else:
        error = ERROR_PASSWORD_CONFIRM_NOT_IDENTICAL

    return error

@csrf_exempt
def login_or_registration( request ):
    email = request.POST['email']
    password = request.POST['password']
    password_confirm = request.POST.get('password_confirm', None)

    if password_confirm is None:
        error = _login( request, email, password )
    else:
        error = _registration( email, password, password_confirm )

    if error is None:
        return HttpResponse( json.dumps( _makeJsonResponse( True, None ) ), content_type="application/json" )
    else:
        return HttpResponse( json.dumps( _makeJsonResponse( False, error ) ), content_type="application/json" )

@csrf_exempt
@login_required
def login_test(request):
    print request.user
    return HttpResponse( request.user.username )

@csrf_exempt
def logout_view(request):
    logout(request)
    return HttpResponse( 'logout success' )