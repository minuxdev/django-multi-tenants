from django.shortcuts import render, redirect
from .forms import LoginForm, SignupForm
from django.contrib.auth.models import User
from .models import Company
from tenant.models import Client, Domain

# Create your views here.

def login_hendler(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']

            try:
                schema_name = Client.objects.get(schema_name=name).schema_name
                if schema_name == name:
                    # return redirect(f'http://{name}.localhost:8000/userspace/')
                    return redirect(f'https://{name}.leeva.up.railway.app/userspace/')
                else:
                    #   Login error message
                    pass
            except Exception as e:
                # User doesnt exist error message
                pass
    
    form = LoginForm(request.GET)
    return render(request, 'login.html', {'form': form})


def signup_hendler(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            check_password = form.cleaned_data['check_password']

            if password == check_password:
                User.objects.create(
                    username = name,
                    password = password
                )
                new_user = User.objects.get(username=name)
                print(new_user)
                tenant = Client.objects.create(
                    schema_name = name,
                    user = new_user,
                    name = name,
                )
                domain = Domain()
                domain.domain = f"{name}.localhost"
                domain.tenant = tenant
                domain.is_primary = True
                domain.save()

                Company.objects.create(
                    name = name,
                    email = email
                )
                
            return redirect('auth:login')
        else:
            form = SignupForm(request.GET)
    else:
        form = SignupForm(request.GET)
    return render(request, 'login.html', {'form': form})