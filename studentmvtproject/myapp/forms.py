from django import forms
from myapp.models import Student


class StudentForm(forms.ModelForm):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()    
    email=forms.EmailField()
    class Meta:
        model = Student
        fields = ['name', 'age', 'email']