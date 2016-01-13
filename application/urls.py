# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^api/', include('api.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
