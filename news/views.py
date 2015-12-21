# -*- coding: utf-8 -*-


from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from models import News
from serializers import NewsSerializer,NewsListSerializer


class NewsListViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = News.objects.all()
        serializer = NewsListSerializer(queryset, many=True)
        return Response(serializer.data)


class NewsDetailViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk):
        queryset = News.objects.all()
        news = get_object_or_404(queryset, pk=pk)
        serializer = NewsSerializer(news)
        return Response(serializer.data)

    def delete(self, request, pk):
        queryset = News.objects.all()
        news = get_object_or_404(queryset, pk=pk)
        news.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

