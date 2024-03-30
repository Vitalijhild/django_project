from django.urls import path, include
from task_app import views

urlpatterns = [
    path('', views.TaskList.as_view(), name='tasklst'),
    path('<int:pk>', views.TaskDetail.as_view(), name='task_detail'),

]