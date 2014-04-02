# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

from forcompany.forms import CompanyInfoForm

def fill_info(request):

    if request.method == 'POST':
        form = CompanyInfoForm(data=request.POST)
        if form.is_valid():
            print 'valid success'

    return render(request, 'fill_info.html', {'form': CompanyInfoForm()})
