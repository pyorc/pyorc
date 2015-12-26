# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128)
    content = models.TextField()
    user_id = models.CharField(max_length=32)
    create_dt = models.DateTimeField(default=timezone.now)
    update_dt = models.DateTimeField(auto_now=True)
    supplement = models.TextField(null=True)

    class Meta:
        db_table = 'question'


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
    question_id = models.IntegerField()
    user_id = models.IntegerField()
    collect_dt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'collection'
        unique_together = ('question_id', 'user_id')


class Start(models.Model):
    user_id = models.IntegerField()
    question_id = models.IntegerField(null=True)
    answer_id = models.IntegerField(null=True)
    flag = models.IntegerField()  # 赞同还是反对, 0:赞同, 1:反对
    update_dt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'start'
        unique_together = ('user_id', 'question_id', 'answer_id')


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
