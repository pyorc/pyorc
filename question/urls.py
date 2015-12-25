# -*- coding: utf-8 -*-


from django.conf.urls import include,url
from rest_framework import routers
from views import QuestionListViewSet, QuestionDetailViewSet

router = routers.SimpleRouter()
router.register(r'question', QuestionListViewSet, base_name='question-list')
router.register(r'question', QuestionDetailViewSet, base_name='question-detail')


urlpatterns = [
    url(r'^', include(router.urls))
]
