from django import forms
from django.contrib.auth.models import User



class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=40)
    email = forms.EmailField()
    password = forms.CharField(max_length=255, widget = forms.PasswordInput)
    password_repeat = forms.CharField(max_length=255, widget = forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists")
            return email

    def clean(self):
        form_data = self.cleaned_data
        if form_data['password'] != form_data['password_repeat']:
            self._errors["password"] = ["Password do not match"] # Will raise a error message
            del form_data['password']
            return form_data


