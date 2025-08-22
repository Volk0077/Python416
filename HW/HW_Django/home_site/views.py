from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Portfolio
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError



def home(request):
    context = {"title": "Главная страница"}
    return render(request, "home_site/home.html", context)


def portfolio_view(request):
    works = Portfolio.objects.all()
    context = {"title": "Стек технологий", "works": works}
    return render(request, "home_site/portfolio.html", context)


def signup_user(request):
    if request.method == "GET":
        return render(
            request, "home_site/signupuser.html", {"form": UserCreationForm()}
        )
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"]
                )
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError: 
                context = {"form": UserCreationForm(), 'error': 'Такое имя пользователя уже существует'}
                return render(
                request, "home_site/signupuser.html", context
                )
        else:
            context = {"form": UserCreationForm(), 'error': 'Пароли не совпадают'}
            return render(
            request, "home_site/signupuser.html", context
            )
        

def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    

def login_user(request):
    if request.method == "GET":
        return render(request, 'home_site/loginuser.html',{'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'home_site/loginuser.html',{'form': AuthenticationForm(), 'error':'Неверные данные для входа'})
        else:
            login(request, user)
            return redirect('home')
