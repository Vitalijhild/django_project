from django.db import models

# Create your models here.
class State(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return str()

class Preoretis(models.Model):
    name = models.CharField(max_length=100)
    value = models.IntegerField()

    def __str__(self) -> str:
        return self.name + " - " + str(self.value)

class Task(models.Model):
    task_name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.ForeignKey(State, on_delete=models.DO_NOTHING)
    prerety = models.ForeignKey(Preoretis, on_delete=models.DO_NOTHING)
    date_start = models.DateTimeField(auto_now_add=True)
    date_finished = models.DateTimeField(auto_now_add=True)
