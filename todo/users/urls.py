from django.urls import path

from . import views

urlpatterns = [
    path('users/', views.TodoUserCreateView.as_view(), name='users'),
    path('users/<int:pk>/', views.TodoUserRetrieveView.as_view(), name='retrieve_users'),
]
