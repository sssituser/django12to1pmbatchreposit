from django.shortcuts import render,redirect
from myapp.models import Student
from myapp.forms import StudentForm
from django.contrib.auth.decorators import *
# Create your views here.

@login_required
def register(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True) # insert into student values(...)
            form = StudentForm()  # Clear the form after saving
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'myapp/register.html', {'form': form})



def students(request):
    students = Student.objects.all() #select * from student
    return render(request, 'myapp/students.html', {'students': students})

def edit(request, id):
    student = Student.objects.get(pk=id)  #select * from student where id=?
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save(commit=True)
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'myapp/edit.html', {'form': form, 'student': student})



def show(request, id):
    student = Student.objects.get(pk=id)
    return render(request, 'myapp/show.html', {'student': student})

def delete(request, id):
    student = Student.objects.get(pk=id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'myapp/delete.html', {'student': student})