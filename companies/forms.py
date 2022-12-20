from django import forms


class EmployeeForm(forms.Form):
    name = forms.CharField(max_length=32)
    email = forms.EmailField(max_length=50, widget=forms.EmailInput)
    salary = forms.CharField(widget=forms.NumberInput)
    status = forms.BooleanField(required=False)
    