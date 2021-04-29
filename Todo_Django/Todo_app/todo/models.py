from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    username = models.ForeignKey(
        User, verbose_name='username', on_delete=models.CASCADE, blank=True, null=True)
    task_name = models.CharField(max_length=100)
    task_description = models.TextField()
    assign_date = models.DateField()

    def __str__(self):
        return self.task_name
