from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^survey/opinion$', 'foradmin.views.survey_opinion_view', name='survey_opinion'),
    url(r'^survey/location$', 'foradmin.views.survey_location_view', name='survey_location'),
    url(r'^survey/category$', 'foradmin.views.survey_category_view', name='survey_category'),
    url(r'^before_payment', 'foradmin.views.before_payment_view', name='before_payment'),
    url(r'^payment_startweb_test', 'foradmin.views.payment_startweb_test_view', name='payment_startweb_test'),
    url(r'^payment_next', 'foradmin.views.payment_next_view', name='payment_next'),
    url(r'^payment_return', 'foradmin.views.payment_return_view', name='payment_return'),
    url(r'^payment_noti', 'foradmin.views.payment_noti_view', name='payment_noti'),
    url(r'^send_mail_test', 'foradmin.views.send_mail_test_view', name='send_mail_test'),
)