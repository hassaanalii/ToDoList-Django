from django.shortcuts import render, redirect
from .forms import TaskForm, CreateUserForm
from .models import Task
from django.contrib import messages
from django.urls import reverse_lazy

# Create your views here.
def login_view(request):
    context = {} 
    return render(request, 'login.html', context)

def registration_view(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request, 'Account has been created for ' + user)
            return redirect("login")

    context = {'form' : form}
    return render(request, 'register.html', context)
def add_task(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid:
            form.save()

    
    return render(request, 'addtask.html', context = {'form' : form})

def view_tasks(request):
    all_tasks = Task.objects.all()
    return render(request, 'viewtasks.html', context = {'all_tasks' : all_tasks, 'request' : request})

def update_task(request, primary_key):
    specific_task = Task.objects.get(id = primary_key)
    form = TaskForm(instance = specific_task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance = specific_task)
        if form.is_valid:
            form.save()

    return render(request, 'addtask.html', context = {'form' : form})

def delete_task(request, primary_key):
    specific_task = Task.objects.get(id = primary_key)
    if request.method == 'POST':
        specific_task.delete()
        return redirect('view-tasks')
    else:
        return redirect('view-tasks')

    