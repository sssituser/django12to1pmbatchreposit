from django.shortcuts import render,redirect
from empapp.forms import EmployeeForm
from empapp.models import Employee


# Create your views here.
def edit(request):
    return render(request,'empapp/edit.html')

def register(request):
    form = EmployeeForm()
    print('Before if statement')
    if request.method == 'POST':
        print('After if statement')
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('emplist')
    print('Iam Navigating to form.html')
    return render(request,'empapp/register.html',{'form':form})


def show(request):
    return render(request,'empapp/show.html')

def employees(request):
    Employees = Employee.objects.all()
    return render(request,'empapp/employee.html',{"emp_list":Employees})



def delete(request):
    return render(request,'empapp/delete.html')

