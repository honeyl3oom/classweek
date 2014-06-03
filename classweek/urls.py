from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^forcompany/', include('forcompany.urls')),
    url(r'^user/', include('user.urls')),
    url(r'^classes/', include('classes.urls')),
    url(r'^foradmin/', include('foradmin.urls')),
    url(r'^analysis/', include('analysis.urls')),
    # url(r'^docs/', include('rest_framework_swagger.urls')),
    # url(r'^$', 'classweek.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)