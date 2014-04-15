# -*- coding: utf-8 -*-
import json
from django.views.decorators.csrf import csrf_exempt

from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, AnonymousUser
from django.db import IntegrityError
from classweek import const, util

from forcompany.forms import CompanyInfoForm

from user.models import UserProfile

# response_data = {}
# response_data['result'] = 'success'
# response_data['message'] = 'registration success'
# return HttpResponse( json.dumps(response_data), content_type="application/json")

# input : username, email, password
# @require_http_methods(["GET", "POST"])

def _makeJsonResponse( isSuccess, error_message, error_code ):
    return_value = {}
    if isSuccess:
        return_value['result'] = util.RESPONSE_STR_SUCCESS
    else:
        return_value['result'] = util.RESPONSE_STR_FAIL
    return_value['error_message'] = error_message
    return_value['error_code'] = error_code
    return return_value

# def _login( request, email, password ):
#
#     error = None
#
#     user = authenticate( username=email, password=password)
#     if user is not None:
#         if user.is_active:
#             login( request, user )
#         else:
#             error = util.ERROR_NOT_ACTIVE_USER
#     else:
#         error = util.ERROR_FAIL_TO_AUTHENTICATE
#
#     return error

def _login( request, email, password ):
    ( error, errorCode )  = (None, 0)

    if not(User.objects.filter( username = email ).exists()):
        (error, errorCode ) = ( const.ERROR_NOT_EXIST_ID , const.CODE_ERROR_NOT_EXIST_ID )
    else:
        user = authenticate( username=email, password=password)
        if user is not None:
            if user.is_active:
                login( request, user )
            else:
                (error, errorCode ) = ( const.ERROR_NOT_ACTIVE_USER , const.CODE_ERROR_NOT_ACTIVE_USER )
        else:
            (error, errorCode ) = ( const.ERROR_PASSWORD_NOT_CORRECT , const.CODE_ERROR_PASSWORD_NOT_CORRECT )

    return (error, errorCode )

def _registration( email, password, password_confirm ):
    ( error, errorCode )  = (None, 0)
    if password == password_confirm:
        try:
            user = User.objects.create_user( email, email, password )
        except ValueError:
            ( error, errorCode ) = (const.ERROR_USERNAME_MUST_BE_SET, const.CODE_ERROR_USERNAME_MUST_BE_SET)
        except IntegrityError:
            ( error, errorCode ) = (const.ERROR_ALREADY_EXIST_USERNAME, const.CODE_ERROR_ALREADY_EXIST_USERNAME)
    else:
        ( error, errorCode ) = (const.ERROR_PASSWORD_CONFIRM_NOT_IDENTICAL, const.CODE_ERROR_PASSWORD_CONFIRM_NOT_IDENTICAL)

    return (error, errorCode )

def _HttpJsonResponse( error, error_code ):
    if error is None:
        return HttpResponse( json.dumps( _makeJsonResponse( True, None, None ) ), content_type="application/json" )
    else:
        return HttpResponse( json.dumps( _makeJsonResponse( False, error, error_code ) ), content_type="application/json" )

@csrf_exempt
def login_view( request ):
    email = request.POST['email']
    password = request.POST['password']

    (error, error_code ) = _login( request, email, password )

    return _HttpJsonResponse( error, error_code )

@csrf_exempt
def registration_view( request ):
    email = request.POST['email']
    password = request.POST['password']
    password_confirm = request.POST.get('password_confirm', None)

    ( error, error_code ) = _registration( email, password, password_confirm )

    return _HttpJsonResponse( error, error_code )

@csrf_exempt
def logout_view(request):
    logout(request)
    return _HttpJsonResponse( None, 0 )

@csrf_exempt
def update_view(request):

    if isinstance(request.user, AnonymousUser):
        return _HttpJsonResponse( util.ERROR_HAVE_TO_LOGIN )

    # userProfile = UserProfile( id=request.user.profile.id, name = request.POST.get('name') )
    # userProfile.save()

    request.user.profile.name = request.POST.get('name')
    request.user.profile.birthday = request.POST.get('birthday')
    request.user.profile.phonenumber = request.POST.get('phonenumber')
    request.user.profile.gender = request.POST.get('gender')
    request.user.profile.save()

    # request.user.profile.update(name = request.POST.get('name'), birthday = request.POST.get('birthday'), phonenumber = request.POST.get('phonenumber'), gender = request.POST.get('gender') )

    # userProfile = UserProfile( id=request.user.profile.id, user_id=request.user.id, name = request.POST.get('name'), birthday = request.POST.get('birthday'), phonenumber = request.POST.get('phonenumber'), gender = request.POST.get('gender') )
    # userProfile.save()

    return _HttpJsonResponse( None )

# @csrf_exempt
# @login_required
# def login_test(request):
#     print request.user
#     return HttpResponse( request.user.username )

