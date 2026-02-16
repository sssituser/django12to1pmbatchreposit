from django.shortcuts import render,redirect

# Create your views here.
def home_view(request):
    return render(request,'myapp/home.html')

def login_view(request):
    if request.method=='POST':
        uname=request.POST.get("username")
        password = request.POST.get("password")
        response = redirect('result')
        response.set_cookie("usr",uname)
        response.set_cookie('pwd',password)
        return response
    return render(request,'myapp/login.html')

def result_view(request):
    uname=request.COOKIES.get("usr")
    password = request.COOKIES.get("pwd")
    return render(request,'myapp/result.html',{'name':uname,'password':password})



