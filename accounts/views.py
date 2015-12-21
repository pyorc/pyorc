from django.contrib.auth.models import User
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from accounts.serializers import UserSerializer


class AccountViewSet(ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def register(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(**serializer.validated_data)
            return Response(user.username, status=201)
        return Response(serializer.errors, status=400)

    def login(self, request):
        return Response()
