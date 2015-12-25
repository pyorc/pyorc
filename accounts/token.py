# coding=utf-8


from uuid import uuid4
from django.core.cache import cache


# TOKEN 失效时间(秒数)
TOKEN_EXPIRE_TIME = 3600


class Token(object):

    @classmethod
    def create_token(cls, user):  # TODO: 同一个用户多次登录如何处理？
        token = uuid4().hex
        cache.set(token, user.id, TOKEN_EXPIRE_TIME)
        return token

    @classmethod
    def get_user(cls, token):
        return cache.get(token)

    @classmethod
    def delete_token(cls, token):
        cache.delete(token)
