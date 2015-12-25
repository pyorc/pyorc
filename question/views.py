# -*- coding: utf-8 -*-


from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from serializers import *
from paginations import QuestionSetPagination
from rest_framework.response import Response


class QuestionDetailViewSet(viewsets.ViewSet):
    queryset = Question.objects.all()

    def retrieve(self, request, pk):
        question = get_object_or_404(self.queryset, pk=pk)
        serializer = QuestionDetailSerializer(question)
        return Response(serializer.data)


class QuestionListViewSet(viewsets.ViewSet):
    queryset = Question.objects.all()
    paginator = QuestionSetPagination()

    def list(self, request):
        page = self.paginator.paginate_queryset(self.queryset, request)
        question = QuestionListSerializer(page, many=True).data
        return self.paginator.get_paginated_response(question)


class StartDetailViewsSet(viewsets.ViewSet):
    pass


class AnswerDetailViewSet(viewsets.ViewSet):
    pass


class CollectionDetailViewSet(viewsets.ViewSet):
    pass
