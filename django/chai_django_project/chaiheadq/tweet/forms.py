from django import forms 
from .models import Tweet
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo'] # list: coz dev designed forms

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username','email','password1','password2') # tuple: coz built-in designed forms

# class SearchTweetForm(forms.ModelForm):
#     class Meta:
#         model = Tweet
#         fields = ['text',] # list: coz dev designed forms