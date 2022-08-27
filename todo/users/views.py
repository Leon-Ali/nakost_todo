from rest_framework import generics

from .serializers import TodoUserSerializer
from .models import TodoUser


class TodoUserCreateView(generics.CreateAPIView):
    """
    API endpoint that allows users to be created.
    """
    queryset = TodoUser.objects.all()
    serializer_class = TodoUserSerializer


class TodoUserRetrieveView(generics.RetrieveAPIView):
    """
    API endpoint that allows users to be viewed.
    """
    queryset = TodoUser.objects.all()
    serializer_class = TodoUserSerializer
