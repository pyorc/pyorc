from django.contrib.auth.models import User
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from accounts.serializers import UserSerializer


class AccountViewSet(ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def register(self, request):
        serializer = UserSerializer(request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(user.username, status=201)
        return Response(serializer.errors, status=400)
