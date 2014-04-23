# -*- coding: utf-8 -*-
from __builtin__ import unicode


class ApiLogger(object):
    def process_view(self, request, view_func, view_args, view_kwargs):
        params_dict = {}
        for key, value in request.POST.iteritems():
            params_dict[key]=value

        print repr(params_dict).decode('unicode-escape').replace("u'","'")

        print view_func
        print view_args
        print view_kwargs
        return None