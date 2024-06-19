from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm

class RegistrationForm(forms.Form):
    username = forms.CharField(label='', max_length=50, widget=forms.TextInput(attrs={'class': 'login', 'placeholder': 'Имя пользователя'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class': 'email', 'placeholder': 'Email'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'password', 'placeholder': 'Пароль'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password']
        )
        return user




class LoginForm(AuthenticationForm):
    username = forms.CharField(label='',max_length=50, widget=forms.TextInput(attrs={'class': 'login', 'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'class': 'password', 'placeholder': 'Пароль'}))