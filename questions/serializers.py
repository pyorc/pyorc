# -*- coding: utf-8 -*-

from rest_framework import serializers
from models import *


class AnswerDetailSerializer(serializers.ModelSerializer):
    starts = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    class Meta:
        model = Answer
        fields = ['answer_id', 'content', 'create_dt', 'user', 'starts']

    def get_starts(self, obj):
        agree = Star.objects.filter(answer_id=obj.answer_id, flag=0).count()
        disagree = Star.objects.filter(answer_id=obj.answer_id, flag=1).count()
        return dict(agree=agree, disagree=disagree)

    def get_user(self, obj):
        return {'a': 'b'}


class AnswerCreateSerialisr(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['question_id', 'content', 'user_id']


class QuestionDetailSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()
    starts = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ['question_id', 'title', 'content', 'user_id',
                  'content', 'create_dt', 'update_dt', 'user', 'starts', 'answers']

    def get_answers(self, obj):
        answers = Answer.objects.filter(question_id=obj.question_id)
        return AnswerDetailSerializer(answers, many=True).data

    def get_starts(self, obj):
        agree = Star.objects.filter(question_id=obj.question_id, flag=0).count()
        disagree = Star.objects.filter(question_id=obj.question_id, flag=1).count()
        return dict(agree=agree, disagree=disagree)

    def get_user(self, obj):
        return {'a': 'b'}

    def get_comments(self, obj):
        comments = Comment.objects.filter(parent_id=obj.question_id)
        return CommentDetailSerializer(comments, many=True).data


class QuestionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['question_id', 'title', 'content', 'user_id']


class QuestionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['question_id', 'title', 'create_dt']


class CommentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment


class StartCreateSerializer(serializers.ModelSerializer):
    flag = serializers.ChoiceField(choices=[0, 1])

    class Meta:
        model = Star
        fields = ['flag']


class CollectionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['parent_id']
