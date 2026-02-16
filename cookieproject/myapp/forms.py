from django import forms
from myapp.models import User

class RegistrationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

        widgets = {
            'password': forms.PasswordInput(),
        }
