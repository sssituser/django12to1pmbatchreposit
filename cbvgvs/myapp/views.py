from django.shortcuts import render
from django.views.generic import *
# Create your views here.
from myapp.models import Employee

class Employees(ListView):
    model=Employee
    fields ='__all__'

class AddEmployee(CreateView):
    model=Employee
    fields='__all__'

class EditEmployee(UpdateView):
    model=Employee
    fields=['EmpName','EmpSal']

class DeleteEmployee(DeleteView):
    model=Employee

class FindEmployee(DetailView):
    model=Employee


