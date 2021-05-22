from django import forms
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Task
from .forms import TaskForm

# Create your views here.


def homepage(request):
    tasks = Task.objects.filter(complete=False)
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(
        request=request,
        template_name='main/home.html',
        context={
            "tasks": tasks,
            "form": form,
        }
    )


def update_task(request, task_name, task_id):
    task = Task.objects.get(id=task_id, title=task_name)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(
        request=request,
        template_name='main/update_task.html',
        context={
            "task": task,
            "form": form,
        }
    )


def delete_task(request, task_name, task_id):
    task = Task.objects.get(id=task_id, title=task_name)

    if request.method == 'POST':
        task.delete()
        return redirect('/')

    return render(
        request=request,
        template_name='main/delete.html',
        context={
            "task": task,
        }
    )
