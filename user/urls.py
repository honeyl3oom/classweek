from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^login_or_registration$', 'user.views.login_or_registration', name='login_or_registration'),
    url(r'^login_test$', 'user.views.login_test', name='login_test'),
    url(r'^logout$', 'user.views.logout_view', name='logout'),
)