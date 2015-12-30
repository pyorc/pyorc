# coding=utf-8


from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from accounts.token import token_required
from topics.models import TopicModel
from topics.serializers import TopicSerializer
from utils.helper import get_paginated_response


class TopicViewSet(ViewSet):

    def list(self, request):
        queryset = TopicModel.objects.all()
        return get_paginated_response(request, queryset, TopicSerializer)

    @token_required
    def create(self, request):
        data = dict(request.data)
        data['user'] = request.user_id
        serializer = TopicSerializer(data=data)
        if serializer.is_valid():
            topic = serializer.save()
            return Response({
                'topic_id': topic.topic_id,
                'created_time': topic.created_time
            }, status=201)
        return Response(serializer.errors, status=422)

    @token_required
    def destroy(self, request, topic_id):
        topic = get_object_or_404(TopicModel, pk=topic_id)
        if topic.user.id != request.user_id:
            return Response(status=403)
        topic.delete()
        return Response(status=204)
