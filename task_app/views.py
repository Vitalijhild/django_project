from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse
from .models import *
from task_app.forms import TaskForm, FilterTaskForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.shortcuts import get_object_or_404

class TaskList(ListView):
    model = Task
    template_name = 'task_app/tasklist.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FilterTaskForm(self.request.GET)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.GET.get("status", 'all')
        if status != 'all':
            try:
                state = get_object_or_404(State, name=status)
                queryset = queryset.filter(status=state)
            except State.DoesNotExist:
                queryset = Task.objects.none()  # Empty queryset
        return queryset

class TaskDetail(DetailView):
    model = Task
    template_name = 'task_app/task_detail.html'
    context_object_name = 'task'

class TaskCreate(LoginRequiredMixin, CreateView):
    
    model = Task
    template_name = 'task_app/task_form.html'
    
    form_class = TaskForm
    success_url = '/'
    def form_valid(self, form):
        form.instance.date_start = form.cleaned_data['date_start']
        form.instance.date_finished = form.cleaned_data['date_finished']
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = "task_app/edit_task.html"
    context_object_name = "task"
    # fields = ['title', 'description']  # a subset of all fields
    # readonly_fields = ['date_modified']  # a subset of the `fields` tuple
    # can also specify form classes here if needed:
    form_class = TaskForm
    success_url = '/'
    def form_valid(self, form):
        form.instance.date_start = form.cleaned_data['date_start']
        form.instance.date_finished = form.cleaned_data['date_finished']
        return super().form_valid(form)