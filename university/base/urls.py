from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # This makes http://127.0.0.1/ load home.html
    path('home/', views.home, name='home'),
    path('web-development/', views.web_development, name='web-development'),
    path('data-science/', views.data_science, name='data-science'),
    path('ai/', views.ai_internship, name='ai-internship'),
    path('about/', views.about, name='about'),
    path('account/', views.account, name='account'),
    path('internships/', views.internships, name='internships'),
    path('aws/',views.aws,name='aws'),
      path('c/', views.c, name='c'),
    path('c++/', views.cpp, name='c++'),
    path('front/', views.front, name='front'),
   path('java/', views.java, name='java'),
  path('ml/', views.ml, name='ml'),
    path('prompt/', views.prompt, name='prompt'),
    path('python/', views.python, name='python'),
    path('tf/', views.tf, name='tf'),

    path('application/', views.application, name='application'),  # Ensure this exists


]
