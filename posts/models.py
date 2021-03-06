# coding=utf-8


from django.db import models
from django.contrib.auth.models import User

from topics.models import TopicModel


class PostModel(models.Model):

    post_id = models.AutoField(primary_key=True)
    topic = models.ForeignKey(TopicModel)
    user = models.ForeignKey(User)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'post'
        ordering = ('created_time', )
