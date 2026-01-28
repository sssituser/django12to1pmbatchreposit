from django.shortcuts import render
from django.views.generic import *
# Create your views here.
class Home(TemplateView):
    template_name='myapp/home.html'
    

class Login(TemplateView):
    template_name = 'myapp/login.html'

class Register(TemplateView):
    template_name = 'myapp/register.html'