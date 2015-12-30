# coding=utf-8


import re
from uuid import uuid4

from django.core.cache import cache
from rest_framework.response import Response


# TOKEN 失效时间(秒数)
TOKEN_EXPIRE_TIME = 3600
# TOKEN 前缀
TOKEN_KEY_PREFIX = 'TOKEN_'
# USER_ID 前缀
USER_ID_KEY_PREFIX = 'USER_ID_'


class Token(object):

    @classmethod
    def create_token(cls, user_id):
        token = uuid4().hex
        cache.set(TOKEN_KEY_PREFIX + token, user_id, TOKEN_EXPIRE_TIME)
        cache.set(USER_ID_KEY_PREFIX + str(user_id), token, TOKEN_EXPIRE_TIME)
        return token

    @classmethod
    def get_user_id_by_token(cls, token):
        user_id = cache.get(TOKEN_KEY_PREFIX + token)
        if not user_id:
            return
        cls._reset_expire_time_by_token(token)  # 更新 token 失效时间
        return int(user_id)

    @classmethod
    def get_token_by_user_id(cls, user_id):
        token = cache.get(USER_ID_KEY_PREFIX + str(user_id))
        return token

    @classmethod
    def _reset_expire_time_by_token(cls, token):
        user_id = cache.get(TOKEN_KEY_PREFIX + token)
        if not user_id:
            return False
        user_id = str(user_id)
        cache.set(TOKEN_KEY_PREFIX + token, user_id, TOKEN_EXPIRE_TIME)
        cache.set(USER_ID_KEY_PREFIX + user_id, token, TOKEN_EXPIRE_TIME)
        return True

    @classmethod
    def delete_token(cls, token):
        user_id = cache.get(TOKEN_KEY_PREFIX + token)
        if not user_id:
            return
        cache.delete(TOKEN_EXPIRE_TIME + token)
        cache.delete(USER_ID_KEY_PREFIX + str(user_id))


def token_required(func):
    def wrapper(viewset, request, *args, **kwargs):
        try:
            request.token = re.match('^token (\w+)', request.META['HTTP_AUTHORIZATION']).groups()[0]
        except (KeyError, AttributeError):
            return Response(status=403)
        request.user_id = Token.get_user_id_by_token(request.token)
        if not request.user_id:
            return Response(status=403)
        return func(viewset, request, *args, **kwargs)
    return wrapper
