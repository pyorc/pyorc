# -*- coding: utf-8 -*-

from rest_framework import serializers
from models import *


class AnswerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer


class QuestionDetailSerializer(serializers.ModelSerializer):
    # question = serializers.StringRelatedField(many=True)
    # question = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    question = AnswerDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['content', 'question']


class QuestionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['question_id', 'title', 'create_dt']


        # class AnswerListSerializer(Ser)
