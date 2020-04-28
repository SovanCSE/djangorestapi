from django import forms
from employee.models import EmployeeProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class EmployeeRegisterFormv1(UserCreationForm):
    email = forms.CharField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=150)
    # password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model= User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data.get('email')
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        # user.password = self.cleaned_data.get('password1')
        # user.username = self.cleaned_data.get('username')

        if commit:
            user.save()
        return user

class EmployeeRegisterFormv2(forms.ModelForm):
    class Meta:
        model = EmployeeProfile
        fields = ['category', 'salary']


class EmployeeLoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
