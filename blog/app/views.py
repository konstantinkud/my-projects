from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
def index_view(request):
    my_data = "Index!"
    return render(request, 'base.html')



from django.contrib.auth import authenticate, login

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Сохраняем форму и получаем объект пользователя
            user = authenticate(request, username=user.username, password=form.cleaned_data['password'])  # Авторизуем пользователя
            if user is not None:
                login(request, user)  # Авторизуем пользователя
                return redirect('index')  # Перенаправление на главную страницу после успешной регистрации и авторизации
    else:
        form = RegistrationForm()
    return render(request, 'registration/registration.html', {'form': form})



def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            print("YES")
            login(request, user)  # Авторизуем пользователя
            return redirect('index')
        else:
            return render(request, 'login/login.html', {'error': "Неправильное имя пользователя или пароль", 'form': form})
    else:
        form = LoginForm()
    return render(request, 'login/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')  


def profile_view(request):
    data = request.user
    return render(request, 'profile/profile.html', context={'data': data})