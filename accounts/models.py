from __future__ import unicode_literals

from django.db import models

from utils.helper import uuid_key


class User(models.Model):

    id = models.CharField(max_length=32, primary_key=True, default=uuid_key)
    username = models.CharField(max_length=32)
    password_hash = models.CharField(max_length=32)
    salt = models.CharField(max_length=32)
    join_time = models.DateTimeField(auto_now=True)


class UserDAO(object):

    @classmethod
    def add_user(cls, username, password_hash, salt):
        User.objects.create(
            username=username,
            password_hash=password_hash,
            salt=salt)
