from django.shortcuts import render
from authentications.models import Company

# Create your views here.


def landing(request):
    return render(request, 'landing.html')


def index(request):
    companies = Company.objects.all()
    print(companies)
    return render(request, 'index.html', {'companies': companies})