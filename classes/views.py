# -*- coding: utf-8 -*-
import json

from classweek import util

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
# from django.core import serializers

from classes.models import Category, SubCategory

def _makeJsonResponse( isSuccess, error_message, data ):
    return_value = {}
    if isSuccess:
        return_value['result'] = util.RESPONSE_STR_SUCCESS
    else:
        return_value['result'] = util.RESPONSE_STR_FAIL
    return_value['error_message'] = error_message
    return_value['data'] = data
    return return_value

def _HttpJsonResponse( error, data ):
    if error is None:
        return HttpResponse( json.dumps( _makeJsonResponse( True, None, data ) ), content_type="application/json" )
    else:
        return HttpResponse( json.dumps( _makeJsonResponse( False, error, data ) ), content_type="application/json" )

@csrf_exempt
def getSubCategory_view( request, category_name ):
    subCategorys = SubCategory.objects.values_list('id','name').filter( category__name = category_name ).all()

    return _HttpJsonResponse( None, json.dumps(subCategorys) )
    # print subCategorys
    # return HttpResponse( category_name )