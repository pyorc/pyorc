# coding=utf-8


from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):

    post_id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, related_name='posts')
    title = models.CharField(max_length=256)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'post'
        ordering = ('-created_time', )
