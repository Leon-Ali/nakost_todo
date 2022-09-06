from django.urls import path

from . import views

urlpatterns = [
    path('tasks/', views.TaskCreateView.as_view(), name='tasks'),
    path('tasks/complete/', views.TasksCompleteView.as_view(), name='tasks_complete'),
]