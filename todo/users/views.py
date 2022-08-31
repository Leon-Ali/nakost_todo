from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from .serializers import TodoUserSerializer
from .models import TodoUser


class TodoUserCreateView(generics.CreateAPIView):
    """
    API endpoint that allows users to be created.
    """
    queryset = TodoUser.objects.all()
    serializer_class = TodoUserSerializer

    def create(self, request, *args, **kwargs):
        user = TodoUser.objects.filter(user_id=request.data['user_id']).first()
        if not user:
            serializer = TodoUserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer = TodoUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TodoUserRetrieveView(generics.RetrieveAPIView):
    """
    API endpoint that allows users to be viewed.
    """
    queryset = TodoUser.objects.all()
    serializer_class = TodoUserSerializer
