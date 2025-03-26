from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('todo.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # For login/logout
    path('', lambda request: redirect('login')),  # Redirect root to login
]