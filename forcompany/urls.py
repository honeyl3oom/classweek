from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^fillinfo$', 'forcompany.views.fill_info', name='fill_info'),
)