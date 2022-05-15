from django import forms

class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    name = forms.CharField(max_length=40)
    surname = forms.CharField(max_length=40)
    email = forms.CharField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)
    passwordAgain = forms.CharField(widget=forms.PasswordInput)