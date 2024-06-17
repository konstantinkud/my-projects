from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login

def index(request):
    my_data = "Index!"
    return render(request, 'index/index.html', {'my_data': my_data})



def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Перенаправление на главную страницу после успешной регистрации
    else:
        form = RegistrationForm()
    return render(request, 'registration/registration.html', {'form': form})



def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # Only call login after successful authentication
                return redirect('index')  # Redirect to the index page after successful login
    else:
        form = LoginForm()
    return render(request, 'login/login.html', {'form': form})