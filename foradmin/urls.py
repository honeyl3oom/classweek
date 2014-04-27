from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^payment_startweb_test', 'foradmin.views.payment_startweb_test_view', name='payment_startweb_test'),
    url(r'^payment_next_test', 'foradmin.views.payment_next_test_view', name='payment_next_test'),
    url(r'^payment_return_test', 'foradmin.views.payment_return_test_view', name='payment_return_test'),
)