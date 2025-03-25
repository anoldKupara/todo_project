from django.urls import path
from .views import task_list, add_task, delete_task, login_view

urlpatterns = [
    path('', login_view, name='login'),  # Set the login view as the default
    path('tasks/', task_list, name='task_list'),
    path('add/', add_task, name='add_task'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
]