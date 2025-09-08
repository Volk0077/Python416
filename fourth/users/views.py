from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from .forms import ProfileForm


def login_user(request):
    if request.user.is_authenticated:
        return redirect('profiles')
    if request.method == "POST":
        username = request.POST['username'].lower()
        password = request.POST['password']
        
        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            messages.error(request, 'Такого пользователя не существует')
            return render(request, "users/login_register.html")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request,"Неверный логин или пароль")

    return render(request, "users/login_register.html")


def logout_user(request):
    logout(request)
    messages.info(request, 'Вы вышли из учетной записи')
    return redirect('login')


def profiles(request):
    prof = Profile.objects.all()
    context = {
        'profiles': prof,
    }
    return render(request, 'users/index.html', context)


def user_profile(request, pk):
    prof = Profile.objects.get(id=pk)
    top_skills = prof.skill_set.exclude(descriptions__exact="")
    other_skills = prof.skill_set.filter(descriptions="")

    context = {
        'profile': prof,
        'top_skills': top_skills,
        'other_skills': other_skills,
    }
    return render(request, 'users/profile.html', context)


def register_user(request):
    page = 'register'
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'Вы успешно зарегистрированы')
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'При регистрации произошла ошибка')


    context ={
        'page': page,
        'form': form
    }
    return render(request, 'users/login_register.html', context)


@login_required(login_url='login')
def user_account(request):
    prof = request.user.profile # доступ текущего пользователя к своему профилю 
    skills = prof.skill_set.all()
    projects = prof.project_set.all()

    context = {
        'profile': prof,
        'skills': skills,
        'projects': projects
    }
    return render(request, 'users/account.html', context)


@login_required(login_url='login')
def edit_account(request):
    profile = request.user.profile # доступ к профилю пользователя
    form = ProfileForm(instance=profile) # отображение уже существующих данных в форме

    if request.method =='POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {
        'form': form
    }
    return render(request, 'users/profile_form.html', context )