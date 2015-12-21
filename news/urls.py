# -*- coding: utf-8 -*-

from django.conf.urls import url

from views import NewsListViewSet, NewsDetailViewSet

urlpatterns = [
    url(r'^news/$',
        NewsListViewSet.as_view({'get': 'list'})),
    url(r'^news/(?P<pk>[0-9]+)$',
        NewsDetailViewSet.as_view({'get': 'retrieve', 'delete': 'delete'})),
]
