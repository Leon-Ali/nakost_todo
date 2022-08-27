from rest_framework import serializers

from .models import TodoUser


class TodoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoUser
        fields = ['user_id']
