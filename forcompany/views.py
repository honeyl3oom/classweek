# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

from forcompany.forms import CompanyInfoForm

def fill_info(request):
    return render(request, 'fill_info.html', {'form': CompanyInfoForm()})
