from datetime import datetime, timedelta

from django.db.models.aggregates import Min
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from django.utils import timezone

from foradmin.models import ApiLog
from utils import response
from classweek import const


@csrf_exempt
def created_view(request):
    start_date_str = request.POST.get('start_date', None)
    end_date_str = request.POST.get('end_date', None)

    if start_date_str is None or end_date_str is None:
        return response.http_response_by_json(const.CODE_ERROR_REQUEST_PARAMS_WRONG)
    else:
        start_date = timezone.make_aware(datetime.strptime(start_date_str+" 00:00:00", "%Y-%m-%d %H:%M:%S"), timezone.get_current_timezone())
        end_date = timezone.make_aware(datetime.strptime(end_date_str+" 00:00:00", "%Y-%m-%d %H:%M:%S") + timedelta(days=1), timezone.get_current_timezone())

        api_logs = ApiLog.objects.values('user_session_id').annotate(created=Min('created'))
        is_created_between_lambda = lambda x: (x['created']-start_date).days >= 0 and (end_date-x['created']).days >= 0
        api_logs = filter(is_created_between_lambda, api_logs)

        user_session_ids = list(map(lambda x: x['user_session_id'], api_logs))

        return response.http_response_by_json(None, {'data':user_session_ids} )

