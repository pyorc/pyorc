# -*- coding: utf-8 -*-

from rest_framework import serializers
from models import *


class AnswerDetailSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Answer
        fields = ['answer_id', 'content', 'create_dt', 'user', 'comments']

    #
    def get_comments(self, obj):
        comments = Comment.objects.filter(parent_id=obj.answer_id)
        return CommentDetailSerializer(comments, many=True).data

    # def get_starts(self, obj):
    #     agree = Star.objects.filter(answer_id=obj.answer_id, flag=0).count()
    #     disagree = Star.objects.filter(answer_id=obj.answer_id, flag=1).count()
    #     return dict(agree=agree, disagree=disagree)

    def get_user(self, obj):
        return {'user_id': 'xiaowang', 'user_name': u'小蛮', 'gravator': 'a.jpeg'}


class AnswerCreateSerialisr(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['content']


class QuestionDetailSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()
    # starts = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    counts = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ['question_id', 'title', 'content', 'user_id',
                  'content', 'create_dt', 'update_dt', 'user', 'answers', 'counts']

    def get_answers(self, obj):
        answers = Answer.objects.filter(question_id=obj.question_id)[0:5]
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

    def get_counts(self, obj):
        count = Answer.objects.count()
        if count % 5 == 0:
            return count / 5
        return count / 5 + 1


class QuestionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['title', 'content']


class QuestionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['question_id', 'title', 'create_dt', 'content']


class CommentDetailSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['comment_id', 'create_dt', 'content', 'user']

    def get_user(self, obj):
        return {'user_id': 'xiaowang', 'user_name': u'小蛮', 'gravator': 'a.jpeg'}


class StartCreateSerializer(serializers.ModelSerializer):
    flag = serializers.ChoiceField(choices=[0, 1])

    class Meta:
        model = Star
        fields = ['flag']


class CollectionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['parent_id']


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content']
