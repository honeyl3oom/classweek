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

# input : username, email, password
# @require_http_methods(["GET", "POST"])

def makeJsonResponse( isSuccess, error_message ):
    data = {}
    if isSuccess:
        data['result'] = RESPONSE_STR_SUCCESS
    else:
        data['result'] = RESPONSE_STR_FAIL
    data['error_message'] = error_message
    return data

@csrf_exempt
def registration(request):
    try:
        user = User.objects.create_user( request.POST['username'] , request.POST['email'], request.POST['password'] )
        response_data = makeJsonResponse( True, None )
    except Exception, e:
        response_data = makeJsonResponse( False, repr(e) )

    return HttpResponse( json.dumps(response_data), content_type="application/json")

@csrf_exempt
def login_view(request):
    # username = request.POST['username']
    username = "parkjuram"
    # password = request.POST['password']
    password = "123"
    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            login( request, user )
            return HttpResponse( json.dumps( makeJsonResponse(True, None)), content_type="application/json")
            # redirect to a success page.

    return HttpResponse( json.dumps( makeJsonResponse(False, None)), content_type="application/json")
    #     else:
    #         # Return a 'disabled account' error message
    # else:
    #     # Return an 'invalid login' error message.

@csrf_exempt
@login_required
def login_test(request):
    print request.user
    return HttpResponse( request.user.username )

@csrf_exempt
def logout_view(request):
    logout(request)
    return HttpResponse( 'logout success' )