from django.urls import path

from . import views

urlpatterns = [
    path('tasks/', views.TaskListCreateView.as_view(), name='tasks'),
    path('tasks/complete/', views.TasksCompleteView.as_view(), name='tasks_complete'),
]