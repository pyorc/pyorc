#!/usr/bin/env python
# coding=utf-8


from django.conf.urls import url

from accounts.views import LoginView


urlpatterns = [
    url(r'^/login/$', LoginView.as_view()),
]
