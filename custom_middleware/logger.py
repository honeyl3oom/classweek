# -*- coding: utf-8 -*-

import base64, M2Crypto
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

from foradmin.models import ApiLog, UserSession

def generate_session_id(num_bytes = 16):
    return str(base64.b64encode(M2Crypto.m2.rand_bytes(num_bytes)))

class ApiCallLogger(object):
    @staticmethod
    def process_view(request, view_func, view_args, view_kwargs):


        # create api log items
        path_name = request.path
        view_name = view_func.func_name

        params_dict = {}

        for key, value in request.POST.iteritems():
            params_dict[key] = value
        request_params = repr(params_dict).decode('unicode-escape').replace("u'","'")

        user_session_id = request.session.get('user_session_id', None)
        if user_session_id is None:
            user_session_id = generate_session_id()

        if hasattr(request, 'user') and request.user.is_authenticated():
            try:
                user_session = UserSession.objects.get(user=request.user)
                user_session_real_id = user_session.user_session_id
                ApiLog.objects.filter(user_session_id=user_session_id).\
                    update(user_session_id=user_session_real_id)

                user_session_id = user_session_real_id

            except ObjectDoesNotExist as e:
                UserSession.objects.create(
                    user=request.user,
                    user_session_id=user_session_id
                )

        request.session['user_session_id'] = user_session_id
        request.session.set_expiry(60 * 60 * 24 * 10000)

        ApiLog.objects.create(
            user_session_id=user_session_id,
            path_name=path_name,
            view_name=view_name,
            request_params=request_params
        )

        return None

    @staticmethod
    def process_response(request, response):
        user_session_id = request.session.get('user_session_id', None)
        if user_session_id is not None:
            if hasattr(request, 'user') and request.user.is_authenticated():
                try:
                    user_session = UserSession.objects.get(user=request.user)
                    user_session_real_id = user_session.user_session_id

                    ApiLog.objects.filter(user_session_id=user_session_id).\
                        update(user_session_id=user_session_real_id)
                    user_session_id = user_session_real_id

                    request.session['user_session_id'] = user_session_id
                    request.session.set_expiry(60 * 60 * 24 * 10000)

                except ObjectDoesNotExist as e:
                    pass

        return response