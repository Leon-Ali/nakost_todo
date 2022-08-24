from django.db import models

from users.models import TodoUser


class Task(models.Model):
    user = models.ForeignKey(TodoUser, on_delete=models.CASCADE)
    finished = models.BooleanField(default=False)
    description = models.CharField(max_length=250)
    date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

