# -*- coding: utf-8 -*-


import re

from django import forms
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from simple_elasticsearch.forms import ElasticsearchForm, ElasticsearchProcessor

from paginations import QuestionSetPagination
from serializers import *


class QuestionSearchForm(ElasticsearchForm):
    title = forms.CharField()

    def get_index(self):
        return 'pyorc'

    def get_type(self):
        return 'question'

    def prepare_query(self):
        match = {}
        for key, value in self.data.items():
            match[key] = value
        return {
            "query": {
                "match":match
            }
        }


class QuestionDetailViewSet(viewsets.ViewSet):
    """
    """
    queryset = Question.objects.all()
    esp = ElasticsearchProcessor()

    """
    """

    def retrieve(self, request, pk):
        question = get_object_or_404(self.queryset, pk=pk)
        serializer = QuestionDetailSerializer(question)
        return Response(serializer.data)

    def destroy(self, request, pk):
        pass
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, pk):
        serializer = QuestionCreateSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            question = get_object_or_404(self.queryset, pk=pk)
            serializer.update(question, request.data)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def search(self, request):
        form = QuestionSearchForm(request.GET)
        self.esp.reset()
        self.esp.add_search(query=form)
        response = self.esp.es.msearch(self.esp.bulk_search_data)
        return Response(data=response, status=status.HTTP_200_OK)


class QuestionListViewSet(viewsets.ViewSet):
    queryset = Question.objects.all()
    paginator = QuestionSetPagination()

    def list(self, request):
        page = self.paginator.paginate_queryset(self.queryset, request)
        question = QuestionListSerializer(page, many=True).data
        return self.paginator.get_paginated_response(question)

    def create(self, request):
        serializer = QuestionCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnswerListViews(viewsets.ViewSet):
    queryset = Question.objects.all()

    def create(self, request, pk):
        serializer = AnswerCreateSerialisr(data=request.data)

        if serializer.is_valid():
            get_object_or_404(self.queryset, pk=pk)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StartListViewsSet(viewsets.ViewSet):
    question_queryset = Question.objects.all()
    answer_queryset = Answer.objects.all()
    start_queryset = Question.objects.all()

    def create(self, request, pk):
        request.user_id = '1'
        serializer = StartCreateSerializer(data=request.data)
        category = re.findall('/(\w*)/', request._request.path)
        category = 0 if category == 'questions' else 1
        queryset = self.question_queryset if 0 == category else self.answer_queryset
        if serializer.is_valid():
            get_object_or_404(queryset, pk=pk)
            star = self.start_queryset.filter(parent_id=pk, user_id=request.user_id, category=category)
            if star:
                return Response(status=status.HTTP_204_NO_CONTENT)
            serializer.save(**{'category': category, 'user_id': request.user_id,
                               'parent_id': pk})
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnswerDetailViewSet(viewsets.ViewSet):
    pass


class CollectionDetailViewSet(viewsets.ViewSet):
    queryset = Collection.objects.all()

    def destroy(self, request, pk):
        collection = get_object_or_404(self.queryset, question_id=pk, user_id=request.user_id)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CollectionListViewSet(viewsets.ViewSet):
    queryset = Question.objects.all()

    def list(self, request):
        pass

    def update(self, request, pk):
        serializer = CollectionCreateSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
