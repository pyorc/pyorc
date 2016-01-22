from django.db import models
from django.contrib.auth.models import User

from utils.helper import uuid_key


class TopicModel(models.Model):

    topic_id = models.CharField(primary_key=True, max_length=32, default=uuid_key)
    user = models.ForeignKey(User)
    title = models.CharField(max_length=64)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'topic'
        ordering = ('-updated_time',)
