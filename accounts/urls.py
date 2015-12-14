#!/usr/bin/env python
# coding=utf-8


from django.conf.urls import url

from accounts.views import AuthenticationView


urlpatterns = [
    url(r'^/authentication$', AuthenticationView.as_view()),
]
