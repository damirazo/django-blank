# coding: utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin

__author__ = 'damirazo <me@damirazo.ru>'


urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
)