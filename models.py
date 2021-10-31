from django.db import models
from django.db.models.fields import DateTimeField

# Create your models here.

class Task(models.Model):

    Task_details = models.CharField(max_length=50)
    Task_description = models.CharField(max_length=300)
    date = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Task_details