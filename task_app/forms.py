from django import forms
from task_app.models import Task, State
from django.contrib.admin import widgets  
from django.contrib.admin.widgets import AdminDateWidget

class TaskForm(forms.ModelForm):
    date_start = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    date_finished = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Task
        fields = ['task_name', 'description', 'status', 'preorety']
 
class FilterTaskForm(forms.Form):
    print(list(State.objects.all()))
    result = []
    for  i in State.objects.all():
       result.append((i.name, i.name))
    
    status = forms.ChoiceField(choices=result, required=False, label='Статус')