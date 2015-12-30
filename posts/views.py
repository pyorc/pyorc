from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from accounts.token import token_required
from posts.models import PostModel
from posts.serializers import PostSerializer
from topics.models import TopicModel
from utils.helper import get_paginated_response


class PostViewSet(ViewSet):

    def list(self, request, topic_id):
        queryset = PostModel.objects.filter(topic_id=topic_id)
        return get_paginated_response(request, queryset, PostSerializer)

    @token_required
    def create(self, request, topic_id):
        topic = get_object_or_404(TopicModel, pk=topic_id)
        data = dict(request.data)
        data['topic'] = topic.topic_id
        data['user'] = request.user_id
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            post = serializer.save()
            return Response({'post_id': post.post_id}, status=201)
        return Response(serializer.errors, status=422)

    @token_required
    def delete(self, request, topic_id, post_id):
        post = get_object_or_404(PostModel, pk=post_id)
        if post.user.id != request.user_id:
            return Response(status=403)
        post.delete()
        return Response(status=204)
