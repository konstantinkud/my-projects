from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Имя пользователя', max_length=50)
    email = forms.EmailField(label='Электронная почта')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

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
    username = forms.CharField(label='Имя пользователя', max_length=50)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)