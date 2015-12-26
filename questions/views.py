# -*- coding: utf-8 -*-


from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from serializers import *
from paginations import QuestionSetPagination
from rest_framework.response import Response
from rest_framework import status


class QuestionDetailViewSet(viewsets.ViewSet):
    queryset = Question.objects.all()

    def retrieve(self, request, pk):
        question = get_object_or_404(self.queryset, pk=pk)
        serializer = QuestionDetailSerializer(question)
        return Response(serializer.data)

    def destroy(self, request, pk):
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, pk):
        serializer = QuestionCreateSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            question = get_object_or_404(self.queryset, pk=pk)
            serializer.update(question, request.data)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

    def create(self, request, pk):
        # serializer =
        serializer = StartCreateSerializer(request.data)
        # print serializer['content']
        print serializer.__dict__
        # get_object_or_44(self.question_queryset, pk=pk)
        # get_object_or_404(self.answer_queryset, pk=pk)

        return Response()


class AnswerDetailViewSet(viewsets.ViewSet):
    pass


class CollectionDetailViewSet(viewsets.ViewSet):
    pass
