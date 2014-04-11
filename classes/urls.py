from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^(\w+)\/$', 'classes.views.getSubCategory_view', name='getSubCategory'),
)