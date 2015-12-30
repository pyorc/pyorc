from rest_framework import serializers

from posts.models import PostModel


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostModel
        fields = ('post_id', 'topic', 'user', 'content', 'created_time', 'updated_time')
        readonly_fields = ('created_time', 'updated_time')
