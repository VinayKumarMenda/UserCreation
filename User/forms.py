from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserRigisterForm(UserCreationForm):
    email=forms.EmailField(required=False)
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']
        
        
class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email']
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model =Profile 
        fields = ['image']