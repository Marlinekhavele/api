from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models
from django.forms import ModelForm
from models import Student

from django.contrib.auth import(
    authenticate,
    login
   
)

# class UserLoginForm(forms.Form):
#     username = forms.CharField(max_length=40)
#     email = forms.EmailField()
#     password = forms.CharField(max_length=255, widget = forms.PasswordInput)
#     password_repeat = forms.CharField(max_length=255, widget = forms.PasswordInput)

#     def clean_email(self):
#         email = self.cleaned_data['email']
#         if User.objects.filter(email=email).exists():
#             raise ValidationError("Email already exists")
#             return email

#     def clean(self):
#         form_data = self.cleaned_data
#         if form_data['password'] != form_data['password_repeat']:
#             self._errors["password"] = ["Password do not match"] # Will raise a error message
#             del form_data['password']
#             return form_data

# class StudentForm(ModelForm):
#     class Meta:
#         model = Student
#         fields =['user','phone_number','country','county','school']

class Student_Login(forms.Form):
    """
    It's a login form
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


    def clean(self,*args,**kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        #Ensuring the user and password entered
        if username and password:
            #check if username and password are correct
            user = authenticate(username=username,password=password)
            if not user:
                raise forms.ValidationError("sorry username/password is incorrect")
            if not user.check_password(password):
                raise ValidationError("password is wrong")
        return super(Student_Login, self).clean(*args,**kwargs)

class Student_Signup(forms.ModelForm):
    """
    This a signup form
    """
    class Meta:
        model = Student
        fields =['user','phone_number','country','county','school']
        widgets = {
            'user': forms.TextInput(attrs={'required': True}),
            'phone_number': forms.TextInput(attrs={'required': True}),
            'country': forms.TextInput(attrs={'required': True}),
            'county': forms.TextInput(attrs={'required': True}),
            'school': forms.TextInput(attrs={'required': True}),

        }

