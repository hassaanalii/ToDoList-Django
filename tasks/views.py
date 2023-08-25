from django.shortcuts import render, redirect
from .forms import TaskForm, CreateUserForm
from .models import Task
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_view(request):
    context = {} 
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('landing-page')
        else:
            messages.info(request, 'Username or Password is incorrect!')
            return render(request, 'login.html', context)
        
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

@login_required(login_url = 'login')
def landing_page(request):
    return render(request, 'landingpage.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url = 'login')
def add_task(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('view-tasks')

    
    return render(request, 'addtask.html', context = {'form' : form})

@login_required(login_url = 'login')
def view_tasks(request):
    all_tasks = Task.objects.all()
    return render(request, 'viewtasks.html', context = {'all_tasks' : all_tasks, 'request' : request})

@login_required(login_url = 'login')
def update_task(request, primary_key):
    specific_task = Task.objects.get(id = primary_key)
    form = TaskForm(instance = specific_task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance = specific_task)
        if form.is_valid:
            form.save()
            return redirect('view-tasks')

    return render(request, 'addtask.html', context = {'form' : form})


def delete_task(request, primary_key):
    specific_task = Task.objects.get(id = primary_key)
    if request.method == 'POST':
        specific_task.delete()
        return redirect('view-tasks')
    else:
        return redirect('view-tasks')

    