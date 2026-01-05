from django.shortcuts import render

# Create your views here.

def home(request):
    dict ={'name':"Arun","age":"40","course":"Django"}
    return render(request,'myapp/home.html',dict)

