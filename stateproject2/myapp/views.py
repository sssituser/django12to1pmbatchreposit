from django.shortcuts import render,redirect

# Create your views here.
def login_view(request):
    if request.method=="POST":
        usr=request.POST.get("uname")
        pawd = request.POST.get("pwd")

        response = redirect('/home/')
        response.set_cookie("username",usr,max_age=30)
        response.set_cookie("password",pawd,max_age=30)
        return response
    return render(request,'myapp/login.html')

def home_view(request):
    uname = request.COOKIES.get("username")
    paswd  = request.COOKIES.get("password")
    return render(request,'myapp/home.html',{"username":uname,"password":paswd})

def result_view(request):
    uname = request.COOKIES.get("username")
    paswd  = request.COOKIES.get("password")
    return render(request,'myapp/result.html',{"username":uname,"password":paswd})
