from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, max_length=128)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
