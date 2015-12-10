from __future__ import unicode_literals

from django.db import models


class User(models.Model):

    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=32)
    password_hash = models.CharField(max_length=64)
    join_time = models.DateTimeField(auto_now=True)
