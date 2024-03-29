"""
URL configuration for ToDoList project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tasks.views import *

urlpatterns = [
    path('arbisoft/', admin.site.urls),
    path('login/', login_view, name = 'login'),
    path('logout/', logoutUser, name = 'logout'),
    path('landing-page/', landing_page, name = 'landing-page'),
    path('register/', registration_view, name = 'register'),
    path('add-task/', add_task, name = 'add-task'),
    path('view-tasks/', view_tasks, name = "view-tasks"),
    path('update-task/<int:primary_key>', update_task, name = 'update-task'),
    path('delete-task/<int:primary_key>', delete_task, name = 'delete-task'),
    path("__reload__/", include("django_browser_reload.urls")),


]
