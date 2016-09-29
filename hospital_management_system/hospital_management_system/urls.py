from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hospital_management_system.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^rtc/', include('rtc.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
