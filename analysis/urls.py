from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^created$', 'analysis.views.created_view', name='created'),
    # url(r'^took_before$', 'classes.views.took_before_view', name='took_before'),
    # url(r'^([A-Za-z_]+)$', 'classes.views.get_sub_category_list_view', name='getSubCategoryList'),
)
