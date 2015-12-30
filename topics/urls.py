# coding=utf-8


from django.conf.urls import url

from topics.views import TopicViewSet


topic_detail = TopicViewSet.as_view(actions={'delete': 'destroy'})
topic_list = TopicViewSet.as_view(actions={'get': 'list', 'post': 'create'})


urlpatterns = [
    url(r'^$', topic_list),
    url(r'^/(?P<topic_id>\w+)$', topic_detail),
]
