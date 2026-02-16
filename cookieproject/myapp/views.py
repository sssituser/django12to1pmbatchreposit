from django.shortcuts import render,redirect,get_object_or_404,get_list_or_404
from myapp.forms import RegistrationForm
from myapp.models import User
# Create your views here.

def register_view(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('login')
    return render(request,'myapp/register.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        print("Post method executed")
        uname = request.POST.get("username")
        pawd = request.POST.get("password")
        print(f'username : {uname}\nPassword : {pawd}')
        return redirect('profile')
    return render(request,'myapp/login.html')

def profile_view(request):
    return render(request,'myapp/profile.html')
