from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^users/', include('users.urls', namespace="users")),
    url(r'^admin/', include(admin.site.urls)),
)
