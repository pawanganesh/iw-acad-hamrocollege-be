from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField

from django.utils.translation import gettext,gettext_lazy as _
from account.models import User

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','is_admin','is_teacher', 'is_librarian','is_student','is_staff']
        labels={'first_name': 'First Name','last_name':'Last Name','email': 'Email'}
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),'first_name':forms.TextInput(attrs={'class':'form-control'}),'last_name':forms.TextInput(attrs={'class':'form-control'}),'email':forms.EmailInput(attrs={'class':'form-control'}),
        }