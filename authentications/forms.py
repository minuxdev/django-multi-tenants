from django import forms



class LoginForm(forms.Form):
    name = forms.CharField(max_length=32)
    password = forms.CharField(max_length=16, widget=forms.PasswordInput)


class SignupForm(forms.Form):
    name = forms.CharField(max_length=32)
    email = forms.EmailField(max_length=50, widget=forms.EmailInput)
    password = forms.CharField(max_length=16, widget=forms.PasswordInput)
    check_password = forms.CharField(max_length=16, widget=forms.PasswordInput)
    