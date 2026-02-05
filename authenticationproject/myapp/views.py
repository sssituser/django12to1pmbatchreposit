from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

def home(request):
    return render(request,'myapp/home.html')
@login_required
def python_exam_view(request):
    return render(request,'myapp/pythonexam.html')
@login_required
def java_exam_view(request):
    return render(request,'myapp/javaexam.html')

def logout_view(request):
    logout(request)
    return render(request,'myapp/logout.html')

from myapp.forms import RegistrationForm
from django.http import HttpResponseRedirect
def register_view(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'myapp/register.html',{'form':form})