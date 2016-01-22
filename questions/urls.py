# -*- coding: utf-8 -*-


from django.conf.urls import include, url
from rest_framework import routers
from views import *

router = routers.SimpleRouter()
router.register(r'questions', QuestionListViewSet, base_name='question-list')
router.register(r'questions', QuestionDetailViewSet, base_name='question-detail')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'questions/(?P<pk>[0-9]+)/answers$', AnswerListViews.as_view({
        'post': 'create', 'get': 'list'
    })),
    url(r'questions|answers/(?P<pk>[0-9]+)/starts$', StartListViewsSet.as_view({
        'post': 'create'
    })),
    # url(r'questions/(?P<pk>[0-9]+)/answers')
    url(r'search$', QuestionDetailViewSet.as_view({
        'get': 'search'
    })),
    url(r'answers/(?P<pk>[0-9]+)/comments$', CommentListViewSet.as_view({
        'post': 'create'
    })),
    url(r'comments/(?P<pk>[0-9]+)/comments$', CommentListViewSet.as_view({
        'post': 'create'
    }))

]
