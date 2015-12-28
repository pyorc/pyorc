# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone
from simple_elasticsearch.mixins import ElasticsearchIndexMixin
from django.db.models.signals import post_save, pre_delete


class Question(models.Model, ElasticsearchIndexMixin):
    question_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128)
    content = models.TextField()
    user_id = models.CharField(max_length=32)
    create_dt = models.DateTimeField(default=timezone.now)
    update_dt = models.DateTimeField(auto_now=True)
    supplement = models.TextField(null=True)

    class Meta:
        db_table = 'question'

    @classmethod
    def get_index_name(cls):
        return 'pyorc'

    @classmethod
    def get_type_name(cls):
        return 'question'

    @classmethod
    def get_document(cls, obj):
        return {
            'question_id': obj.question_id,
            'title': obj.title,
            'content': obj.content,
            'user_id': obj.user_id,
            'create_dt': obj.create_dt,
            'update_dt': obj.update_dt,
            'supplement': obj.supplement
        }

    @classmethod
    def get_bulk_index_limit(cls):
        return 10

    @classmethod
    def get_queryset(cls):
        return Question.objects.all()

    @classmethod
    def get_request_params(cls, obj):
        return {'routing': obj.user_id}


class Answer(models.Model):
    answer_id = models.AutoField(primary_key=True)
    question_id = models.IntegerField()  # 外键 问题id
    content = models.TextField()
    create_dt = models.DateTimeField(default=timezone.now)
    update_dt = models.DateTimeField(auto_now=True)
    user_id = models.CharField(max_length=32)

    class Meta:
        db_table = 'answer'


class Collection(models.Model):
    parent_id = models.IntegerField()
    user_id = models.IntegerField()
    collect_dt = models.DateTimeField(auto_now=True)
    category = models.IntegerField()

    class Meta:
        db_table = 'collection'
        unique_together = ('parent_id', 'user_id', 'category')


class Star(models.Model):
    user_id = models.IntegerField()
    parent_id = models.IntegerField()  #
    category = models.IntegerField()  # 0表示question 1 表示回答
    flag = models.IntegerField()  # 赞同还是反对, 0:赞同, 1:反对
    update_dt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'star'
        unique_together = ('user_id', 'parent_id', 'category')


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    parent_id = models.IntegerField()
    content = models.TextField()
    user_id = models.CharField(max_length=32)
    category = models.IntegerField()
    flag = models.IntegerField()
    create_dt = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'comment'


post_save.connect(Question.save_handler, sender=Question)
pre_delete.connect(Question.delete_handler, sender=Question)
