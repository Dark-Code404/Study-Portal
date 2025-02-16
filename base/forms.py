from django.forms import ModelForm, modelform_factory
 
from django import forms

from base.models import *
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class RoomForm(ModelForm):
    class Meta:
        model =Room
        fields='__all__'
        exclude=['host','participants','topic']


class MessageForm(ModelForm):
    class Meta:
        model =Message
        fields = ['body', 'image']


class EditProfile(ModelForm):
    class Meta:
        model=User
        fields=['username','name','email','bio','pic']
      
        