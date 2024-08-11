from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.urls import path
from employeeapp import views

urlpatterns = [
    # path('add_address/', views.add_address, name='add_address'),
    # path('test_path/', views.check_employee_app, name='test_path'),
    path('employee/', views.index, name='index'),
    path('add_an_employee/', views.createEmployee, name='add_an_employee'),
    path('update_employee/<int:id>', views.updateEmployee, name='update_employee'),
    path('get_employee_list/', views.getEmployeeList, name='get_employee_list'),
    path('delete_an_employee/<int:id>', views.deleteEmployee, name='delete_an_employee'),
    path('get-employee/<int:id>/', views.get_employee, name='get_employee'),



]