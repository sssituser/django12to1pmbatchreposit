from django.urls import reverse_lazy
from django.views.generic import *
from myapp.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

class StudentList(ListView):
    model=Student
    fields ='__all__'

class CreateStudent(CreateView):
    model = Student
    fields = '__all__'

class StudentDetails(DetailView):
    model = Student

class UpdateStudent(UpdateView):
    model = Student
    fields =['StudentId','StudentName','StudentMarks']

class DeleteStudent(DeleteView):
    model=Student
    success_url = reverse_lazy('list')



