from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("<h1 style='text-align:center'>Home Page</h1>")


def login(request):
    return HttpResponse("<h1 style='text-align:center'>Login  Page</h1>")

def register(request):
    return HttpResponse("<h1 style='text-align:center'>Register Page</h1>")

def about(request):
    return HttpResponse("<h1 style='text-align:center'>About Page</h1>")

def contact(request):
    return HttpResponse("<h1 style='text-align:center'>Contact Page</h1>")
