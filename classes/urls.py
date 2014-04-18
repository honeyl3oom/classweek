from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^([A-Za-z_]+)$', 'classes.views.getSubCategoryList_view', name='getSubCategoryList'),
    url(r'^([A-Za-z_]+)\/([A-Za-z_]+)$', 'classes.views.getClassesList_view', name='getClassesList'),
    url(r'^([A-Za-z_]+)\/([A-Za-z_]+)\/(\d+)$', 'classes.views.getClassesList_view', name='getClassesList'),
    url(r'^(\d+)\/(\d+)$', 'classes.views.getClassesDetail_view', name='inquire'),
    url(r'^(\d+)\/inquire$', 'classes.views.inquire_view', name='inquire'),
)