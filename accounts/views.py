# coding=utf-8


from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from accounts.serializers import UserSerializer
from accounts.token import Token


class AccountViewSet(ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def register(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(**serializer.validated_data)
            token = Token.create_token(user.id)
            data = {
                'username': user.username,
                'token': token
            }
            return Response(data, status=201)
        return Response(serializer.errors, status=400)

    def authentication(self, request):
        # 缺失用户名或密码
        if 'username' not in request.data or 'password' not in request.data:
            return Response(status=400)
        user = authenticate(
            username=request.data['username'],
            password=request.data['password'])
        # 用户验证失败
        if not user:
            return Response(status=401)
        token = Token.get_token_by_user_id(user.id)
        # 若已有token，则删除原有token，重新生成token
        if token:
            Token.delete_token(token)
        token = Token.create_token(user.id)
        return Response(data={'token': token}, status=200)


def token_required(func):
    def wrapper(viewset, request, *args, **kwargs):
        print request
        return func(viewset, request, *args, **kwargs)
    return wrapper()
