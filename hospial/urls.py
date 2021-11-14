"""hspapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path("login_load/",views.login_load),
    path("admin_add_shedule_load/",views.admin_add_shedule_load),
    path("admin_add_doctor_load/", views.admin_add_doctor_load),
    path("admin_add_staff_load/", views.admin_add_staff_load),
    path("admin_add_dept_load/", views.admin_add_dept_load),
    path("admin_adminviewdept_load/",views.admin_adminviewdept_load),
    path("admin_edit_dept/",views.admin_edit_dept),
    path("admin_edit_staff/",views.admin_edit_staff),
    path("admin_edit_doctor/", views.admin_edit_doctor),
    path("admin_edit_schedule/", views.admin_edit_schedule),
    path("admin_leave_req/", views.admin_leave_req),
    path("admin_view_attends/", views.admin_view_attends),
    path("admin_view_doctor/", views.admin_view_doctor),
    path("admin_view_shedule/", views.admin_view_shedule),
    path("admin_view_staff/", views.admin_view_staff),
    path("admin_view_attends/", views.admin_view_attends),
    path("admin_home/", views.admin_Home),


]