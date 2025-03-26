from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def task_list(request):
    active_tasks = Task.objects.filter(completed=False)
    completed_tasks = Task.objects.filter(completed=True)
    return render(request, 'todo/task_list.html', {
        'active_tasks': active_tasks,
        'completed_tasks': completed_tasks
    })

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:  # Ensure title is not empty
            Task.objects.create(title=title)
            return redirect('task_list')  # Redirect to task list after adding task

    # Handle GET request by returning the form
    return render(request, 'todo/add_task.html')

def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')