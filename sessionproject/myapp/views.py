from django.shortcuts import render,redirect

# Create your views here.

def home_view(request):
    username=request.session.get("usr")
    return render(request,'myapp/home.html',{'name':username})

def login_view(request):
    if request.method=='POST':
        username = request.POST["uname"]
        password = request.POST["pwd"]
        if username=="arun" and password=="1234":
            request.session["usr"]=username
            return redirect('home')
        else:
            return render(request,'myapp/login.html',{"error":"Invalid UserName or Password"})
    return render(request,'myapp/login.html')

def logout_view(request):
    return render(request,'myapp/logout.html')