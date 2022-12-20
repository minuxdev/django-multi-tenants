from django.urls import path
from . import views

app_name = 'company'

urlpatterns = [
    path('', views.list_employees, name='list'),
    path('add-employee/', views.add_employee, name='add-employee'),
]