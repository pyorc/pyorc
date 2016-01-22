# -*- coding: utf-8 -*-


from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from models import News
from paginations import NewsSetPagination
from serializers import NewsDetailSerializer, NewsListSerializer


class NewsListViewSet(viewsets.ViewSet):
    paginator = NewsSetPagination()
    queryset = News.objects.all().order_by('-news_id')

    def list(self, request, **kwargs):
        page = self.paginator.paginate_queryset(self.queryset, request)
        news = NewsListSerializer(page, many=True).data
        return self.paginator.get_paginated_response(news)

        # def create(self, request):
        #     # todo
        #     return Response(status=status.HTTP_201_CREATED)


class NewsDetailViewSet(viewsets.ViewSet):
    queryset = News.objects.all()

    def retrieve(self, request, pk):
        news = get_object_or_404(self.queryset, pk=pk)
        serializer = NewsDetailSerializer(news)
        return Response(serializer.data)

    def destroy(self, request, pk):
        get_object_or_404(self.queryset, pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request):
        pass
