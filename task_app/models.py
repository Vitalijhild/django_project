from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class State(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return str(self.name)

class Preoretis(models.Model):
    name = models.CharField(max_length=100)
    value = models.IntegerField()

    def __str__(self) -> str:
        return self.name + " - " + str(self.value)

class Task(models.Model):
    task_name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.ForeignKey(State, on_delete=models.DO_NOTHING)
    preorety = models.ForeignKey(Preoretis, on_delete=models.DO_NOTHING)
    date_start = models.DateTimeField(blank=True, null=True)
    date_finished = models.DateTimeField(blank=True, null=True)

    creator = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL) #who created the task

    def __str__(self):
        return f"{self.task_name} ({self.status})"
    
