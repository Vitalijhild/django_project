from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import *

# Create your views here.
class TaskList(ListView):
    model = Task
    template_name = 'task_app/tasklist.html'
    context_object_name = 'tasks'

class TaskDetail(DetailView):
    model = Task
    template_name = 'task_app/task_detail.html'
    context_object_name = 'task'

class TaskCreate(CreateView):
    model = Task
    template_name = 'task_app/add_task.html'
    fields = '__all__'
    success_url = reverse_lazy('task_list')