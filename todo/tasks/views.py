from typing import List

from rest_framework import generics, status
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from .serializers import TaskSerializer
from .models import Task


class TaskListCreateView(generics.ListCreateAPIView):
    """
    API endpoint that allows tasks created or retrieved.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'date', 'finished']


class TasksCompleteView(generics.CreateAPIView):
    """
    API endpoint for completing tasks by ids.
    """
    serializer_class = TaskSerializer

    def get_queryset(self, ids=List[int]):
        return Task.objects.filter(id__in=ids)

    def create(self, request, *args, **kwargs):
        instances = self.get_queryset(request.data.get('ids'))

        for instance in instances:
            instance.finished = True

        Task.objects.bulk_update(instances, ['finished'])

        return Response(status=status.HTTP_201_CREATED)


