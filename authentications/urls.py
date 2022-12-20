from django.urls import path
from . import views

app_name = 'auth'

urlpatterns = [
    path('', views.login_hendler, name='login'),
    path('signup/', views.signup_hendler, name='signup'),
]