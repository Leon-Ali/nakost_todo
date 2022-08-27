from django.db import models


class TodoUser(models.Model):
    user_id = models.CharField(max_length=100, primary_key=True)

