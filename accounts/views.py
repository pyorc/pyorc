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
            token = Token.create_token(user)
            data = {
                'username': user.username,
                'token': token
            }
            return Response(data, status=201)
        return Response(serializer.errors, status=400)

    def authentication(self, request):
        if 'username' in request.data and 'password' in request.data:
            user = authenticate(
                username=request.data['username'],
                password=request.data['password'])
            if not user:
                return Response()
            token = Token.create_token(user)
            return Response(data={
                'token': token
            }, status=200)
        return Response(status=400)
