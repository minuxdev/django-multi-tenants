from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm

# Create your views here.


def list_employees(request):
    employees = Employee.objects.all()
    return render(request, 'employees.html', {'employees': employees})


def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            employee = Employee.objects.create(
                name = name,
                email = email,
            )
            return redirect('company:list')

    form = EmployeeForm(request.GET)
    return render(request, 'new-employee.html', {'form': form})