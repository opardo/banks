from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^users/', include('users.urls')),
    url(r'^users/admin/', include(admin.site.urls)),
)

