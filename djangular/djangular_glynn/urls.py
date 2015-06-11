from django.conf.urls import include, url, patterns
from django.contrib import admin
from tastypie.api import Api
from jobs.api import JobResource

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangular_glynn.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(v1_api.urls)),
)
