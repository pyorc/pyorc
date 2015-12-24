# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from rest_framework import routers

from views import NewsListViewSet, NewsDetailViewSet

router = routers.SimpleRouter()
router.register(r'news', NewsListViewSet, base_name='news-list')
router.register(r'news', NewsDetailViewSet, base_name='news-detail')


urlpatterns = [
    url(r'^', include(router.urls))
]
