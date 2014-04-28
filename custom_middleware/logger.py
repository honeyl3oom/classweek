# -*- coding: utf-8 -*-

import base64, M2Crypto
from django.db import IntegrityError

from foradmin.models import ApiLog, UserSession

def generate_session_id(num_bytes = 16):
    return str(base64.b64encode(M2Crypto.m2.rand_bytes(num_bytes)))

class ApiLogger(object):
    @staticmethod
    def process_view(request, view_func, view_args, view_kwargs):
        params_dict = {}
        for key, value in request.POST.iteritems():
            params_dict[key] = value

        path_name = request.path
        view_name = view_func.func_name
        user_session_id = request.session.get('user_session_id', None)
        if user_session_id is None:
            user_session_id = generate_session_id()
            request.session['user_session_id'] = user_session_id
            request.session.set_expiry(60 * 60 * 24 * 10000)
        request_params = repr(params_dict).decode('unicode-escape').replace("u'","'")

        if hasattr(request, 'user'):
            if request.user.is_authenticated():
                user_session = UserSession(user=request.user, user_session_id=user_session_id)
                try:
                    user_session.save()
                except IntegrityError as e:
                    pass

        api_log = ApiLog( user_session_id=user_session_id, path_name=path_name, view_name=view_name, request_params=request_params )
        api_log.save()

        return None

    @staticmethod
    def process_response(request, response):

        if hasattr(request, 'user'):
            if request.user.is_authenticated() and request.session.get('user_session_id', None) is not None:
                user_session = UserSession(user=request.user, user_session_id=request.session.get('user_session_id', None))
                try:
                    user_session.save()
                except IntegrityError as e:
                    pass

        return response