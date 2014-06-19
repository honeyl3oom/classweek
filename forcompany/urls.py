from django.conf.urls import patterns, url

from .views import IndexView, CompanyClassesCreateView, CompanyClassesUpdateView, CompanyClassesDetailView, \
    CompanyClassesDeleteView, CompanyMasterProfileUpdateView

urlpatterns = patterns('',
    # url(r'^index$', 'forcompany.views.index_view', name='index'),
    url(
        regex=r'^index/$',
        view=IndexView.as_view(),
        name='index'
    ),
    url(
        regex=r'^company/profile/update/(?P<pk>\d+)/',
        view=CompanyMasterProfileUpdateView.as_view(),
        name='company_master_profile_update'
    ),
    url(
        regex=r'^company/classes/create/$',
        view=CompanyClassesCreateView.as_view(),
        name='company_classes_create'
    ),
    url(
        regex=r'^company/classes/delete/(?P<pk>\d+)/',
        view=CompanyClassesDeleteView.as_view(),
        name='company_classes_delete'
    ),
    url(
        regex=r'^company/classes/detail/(?P<pk>\d+)/',
        view=CompanyClassesDetailView.as_view(),
        name='company_classes_detail'
    ),
    url(
        regex=r'^company/classes/update/(?P<pk>\d+)/',
        view=CompanyClassesUpdateView.as_view(),
        name='company_classes_update'
    ),
    # url(
    #     regex=r'^$',
    #     view=views.CompanyUserCreateView.as_view(),
    #     name='company_master_login'
    # ),
    # url(r'^fillinfo$', 'forcompany.views.fill_info', name='fill_info'),
)