from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^location/([A-Za-z_]+)$', 'foradmin.views.location_request_view', name='location_request'),
    url(r'^category/([A-Za-z_]+)$', 'foradmin.views.category_request_view', name='category_request'),
    url(r'^before_payment', 'foradmin.views.before_payment_view', name='before_payment'),
    url(r'^payment_startweb_test', 'foradmin.views.payment_startweb_test_view', name='payment_startweb_test'),
    url(r'^payment_next', 'foradmin.views.payment_next_view', name='payment_next'),
    url(r'^payment_return', 'foradmin.views.payment_return_view', name='payment_return'),
    url(r'^payment_noti', 'foradmin.views.payment_noti_view', name='payment_noti'),
    url(r'^send_mail_test', 'foradmin.views.send_mail_test_view', name='send_mail_test'),
)