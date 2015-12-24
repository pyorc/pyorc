# -*- coding: utf-8 -*-

from rest_framework import serializers
from models import News


class NewsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = News


class NewsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ('news_id', 'title', 'image_url', 'date_time')
