from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^signup$', 'user.views.sign_up', name='sign_up'),
)