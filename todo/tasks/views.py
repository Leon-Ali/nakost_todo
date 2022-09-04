from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import TaskSerializer
from .models import Task


class TaskCreateView(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be created.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'date']


