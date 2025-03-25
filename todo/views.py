from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)  # Get tasks for the logged-in user
    return render(request, 'todo/task_list.html', {'tasks': tasks})

@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title, user=request.user)  # No need to specify completed; it defaults to False
            return redirect('task_list')
    return render(request, 'todo/add_task.html')

@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)  # Ensure the task belongs to the user
    task.delete()
    return redirect('task_list')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('task_list')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'registration/login.html', {'error': 'Invalid credentials'})
    return render(request, 'registration/login.html')