from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('todo.urls')),  # Add 'tasks/' prefix
    path('accounts/', include('django.contrib.auth.urls')),
]