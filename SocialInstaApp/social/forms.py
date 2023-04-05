from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from social.models import UserProfile,Posts,Comments


class RegistrationForm(UserCreationForm):

    class Meta():
        model=User
        fields=["username","password1","password2"]

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())


class UserProfileForm(forms.ModelForm):
    class Meta():
        model=UserProfile
        exclude=("user","followings")

        widgets={
            # "bio":forms.TextInput(attrs={"class":"form-control"}),
            # "profile_pic":forms.(attrs={"class":"form-control"}),
            # "cover_pic":forms.ImageField(attrs={"class":"form-control"}),
            "dob":forms.DateInput(attrs={"class":"form-control","type":"date"})
            # "profile_pic":forms.ImageField(attrs={"class":"form-control"}),
            # "profile_pic":forms.ImageField(attrs={"class":"form-control"}),
            
        }

class PostForm(forms.ModelForm):
    class Meta():
        model=Posts
        fields=["title","image"]

        widgets={
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "image":forms.FileInput(attrs={"class":"form-control"})
            }
