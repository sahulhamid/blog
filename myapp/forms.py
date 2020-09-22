from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Blog

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())
    

gender_choice = [
    ('male','Male'),
    ('female','Female')
]

class ProfileForm(forms.ModelForm):
    gender = forms.CharField(widget=forms.RadioSelect(choices=gender_choice))
    class Meta:
        model = Profile
        fields = ['first_name','last_name','gender','address','phone_number','image']

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['blog']
        