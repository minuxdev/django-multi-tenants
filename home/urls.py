from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.landing, name='landing'),
    path('home/', views.index, name='index'),
]