# -*- coding: utf-8 -*-
import json

from classweek import util

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# from django.core import serializers
from django.db import IntegrityError
from classes.models import Category, SubCategory, Classes, ClassesInquire

def _makeJsonResponse( isSuccess, error_message, data = None ):
    return_value = {}
    if isSuccess:
        return_value['result'] = util.RESPONSE_STR_SUCCESS
    else:
        return_value['result'] = util.RESPONSE_STR_FAIL
    return_value['error_message'] = error_message
    if data is not None:
        return_value['data'] = data

    return return_value

def _HttpJsonResponse( error, data ):
    if error is None:
        return HttpResponse( json.dumps( _makeJsonResponse( True, None, data ) ), content_type="application/json" )
    else:
        return HttpResponse( json.dumps( _makeJsonResponse( False, error, data ) ), content_type="application/json" )

@csrf_exempt
def getSubCategoryList_view( request, category_name ):
    subCategorys = SubCategory.objects.filter( category__name = category_name ).values()

    # print subCategorys

    # json_data = serializers.serialize('json', subCategorys)

    return _HttpJsonResponse( None, json.dumps( list(subCategorys) ) )

@csrf_exempt
def getClassesList_view( request, category_name, subcategory_name, page_num = 1 ):
    classes = Classes.objects.filter( subCategory__name = subcategory_name ).all()
    paginator = Paginator( classes, util.PAGE_PER_COUNT )

    try:
        current_page_classes = paginator.page( page_num )
        return _HttpJsonResponse( None, serializers.serialize('json', current_page_classes))
    except EmptyPage:
        return _HttpJsonResponse( util.RESPONSE_STR_PAGE_END, None)

@csrf_exempt
def inquire_view( request, classes_id ):
    classesInquire = ClassesInquire( classes_id = classes_id, user = request.user, content= request.POST.get('content') )
    # classesInquire.classes_id = classes_id
    try:
        classesInquire.save()
    except IntegrityError, e:
        return HttpResponse( json.dumps( _makeJsonResponse( False, util.RESPONSE_STR_CLASSES_ID_DOES_NOT_EXIST ) ), content_type="application/json" )
    return HttpResponse( json.dumps( _makeJsonResponse( True, None ) ), content_type="application/json" )
