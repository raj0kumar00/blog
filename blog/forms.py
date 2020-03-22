from django import forms
from simplemathcaptcha.fields import MathCaptchaField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
from django.forms import ModelForm, TextInput,EmailInput,PasswordInput
class SignUpForm(UserCreationForm):
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password','id': "nameValidation1"}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password','id': "nameValidation2"}))
    captcha = MathCaptchaField()
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )

        widgets = {
            'username': TextInput(attrs={'class': 'form-control','placeholder': 'Username','id' : 'username',"onchange":"UsernameValidate()"}),
            }

class Createpost(forms.ModelForm): 
    class Meta: 
        model = Post
        fields = ('title','Description','image','status','slug')