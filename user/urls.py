from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^login$', 'user.views.login_view', name='login'),
    url(r'^registration$', 'user.views.registration_view', name='registration'),
    url(r'^logout$', 'user.views.logout_view', name='logout'),
)