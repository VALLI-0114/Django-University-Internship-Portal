from django.shortcuts import render
from .models import Internship


def home(request):
    return render(request, 'base/home.html')

def about(request):
    return render(request, 'base/about.html')

def account(request):
    return render(request, 'base/account.html')

def internships(request):
    return render(request, 'base/internships.html')

def ai_internship(request):
    return render(request, 'base/ai_internship.html')

def aws(request):
    return render(request, 'base/aws.html')

def c(request):
    return render(request, 'base/c.html')

def cpp(request):
    return render(request, 'base/c++.html')

def data_science(request):
    return render(request, 'base/data_science.html')

def front(request):
    return render(request, 'base/front.html')

def java(request):
    return render(request, 'base/java.html')

def ml(request):
    return render(request, 'base/ml.html')

def prompt(request):
    return render(request, 'base/prompt.html')

def python(request):
    return render(request, 'base/python.html')

def tf(request):
    return render(request, 'base/tf.html')

def web_development(request):
    return render(request, 'base/web_development.html')

def application(request):
    return render(request, 'base/application.html')


