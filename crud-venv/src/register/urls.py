from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('employee', views.employe, name='Employee'),
    path('employee_udpate/<int:id>', views.employeUpdate, name='Employee Update'),
    path('employee_delete/<int:id>', views.employeDelete, name='Employee Delete'),
]
