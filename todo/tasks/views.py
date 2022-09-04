from rest_framework import generics

from .serializers import TaskSerializer
from .models import Task


class TaskCreateView(generics.CreateAPIView):
    """
    API endpoint that allows users to be created.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

