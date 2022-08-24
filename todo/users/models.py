from django.db import models


class TodoUser(models.Model):
    username = models.CharField(max_length=32)

