from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^(\w+)\/$', 'classes.views.getSubCategoryList_view', name='getSubCategoryList'),
    url(r'^(\w+)\/(\w+)\/$', 'classes.views.getClassesList_view', name='getClassesList'),
)