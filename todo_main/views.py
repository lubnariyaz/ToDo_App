from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Task

def home(request):
    tasks = Task.objects.filter(is_completed=False)
    tasks_done = Task.objects.filter(is_completed=True)
    context = {
        'tasks': tasks,
        'tasks_done': tasks_done,
    }
    return render(request, 'home.html', context)