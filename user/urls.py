from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^registration$', 'user.views.registration', name='registration'),
    url(r'^login$', 'user.views.login_view', name='login'),
    url(r'^login_test$', 'user.views.login_test', name='login_test'),
    url(r'^logout$', 'user.views.logout_view', name='logout'),
)