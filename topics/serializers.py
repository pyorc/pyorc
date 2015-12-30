# coding=utf-8


from rest_framework.serializers import ModelSerializer

from topics.models import TopicModel


class TopicSerializer(ModelSerializer):
    class Meta:
        model = TopicModel
        fields = ('topic_id', 'user', 'title', 'content', 'created_time', 'updated_time')
        readonly_fields = ('created_time', 'updated_time')
