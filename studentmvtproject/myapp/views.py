from django.shortcuts import render,redirect
from myapp.models import Student
from myapp.forms import StudentForm
# Create your views here.

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