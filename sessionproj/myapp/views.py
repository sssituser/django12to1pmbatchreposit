from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("uname")
        password = request.POST.get("pwd")

        if username == "arun" and password == "1234":
            request.session["usrname"] = username
            request.session.set_expiry(30)
            return redirect('home')
        else:
            return render(request,'myapp/login.html',
                          {"res":"Invalid Credentials"})
    return render(request,'myapp/login.html')


@never_cache
def home_view(request):
    uname = request.session.get("usrname")
    if uname:
        return render(request,'myapp/home.html',{'name':uname})
    else:
        return redirect('login')


@never_cache
def logout_view(request):
    request.session.flush()
    return render(request,'myapp/logout.html')
