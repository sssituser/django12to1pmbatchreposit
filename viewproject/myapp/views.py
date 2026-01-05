from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("<h1 style='text-align:center;color:red'>Welcome home Page</h1>")

def login(request):
    return HttpResponse("<h1 style='text-align:center;color:green'>Welcome Login Page</h1>")

def register(request):
    return HttpResponse("<h1 style='text-align:center;color:blue'>Welcome Register Page</h1>")

def about(request):
    return HttpResponse("<h1>Welcome About Page</h1>")

def contact(request):
    return HttpResponse("<h1>Welcome Contact Page</h1>")