# Stdlib imports
import json

# Core django imports
from django.http.response import HttpResponse

# Third-party app imports

# Import from your apps
from classweek import const

def http_response_by_json(error, json_={}):
    if error is None:
        json_.update({
            'result': 'success'
        })
    else:
        json_.update({
            'result': 'fail',
            'error_code': error,
            'error_message': const.ERROR_CODE_AND_MESSAGE_DICT[error]
        })

    return HttpResponse(json.dumps(json_, ensure_ascii=False), content_type="application/json; charset=utf-8")