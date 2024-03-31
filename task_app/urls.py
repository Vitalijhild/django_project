from django.urls import path
from task_app import views

urlpatterns = [
    path('', views.TaskList.as_view(), name='task_list'),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name='task_detail'),
    path('task/create/', views.TaskCreate.as_view(), name='task-create'),  # Add this line for creating a new task
]
