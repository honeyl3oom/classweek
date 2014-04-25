from django.db import models
from django.contrib.auth.models import User
import datetime


class ApiLog(models.Model):
    user_session_id = models.TextField(null=False, blank=True, default='')
    path_name = models.TextField(null=False, blank=True, default='')
    view_name = models.TextField(null=False, blank=True, default='')
    request_params = models.TextField(null=False, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now)

    def __unicode__(self):
        return 'ApiLog : %r' % self.user_session_id


class UserSession(models.Model):
    user = models.ForeignKey(User, related_name = 'get_sessions')
    user_session_id = models.TextField(null=False, blank=True, default='')

    class Meta:
        unique_together = ("user", "user_session_id")