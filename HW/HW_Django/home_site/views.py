from django.shortcuts import render
from django.http import HttpResponse
from .models import Portfolio


def home(request):
    context = {"title": "Главная страница"}
    return render(request, "home_site/home.html", context)


def portfolio_view(request):
    works = Portfolio.objects.all()
    context = {"title": "Стек технологий", "works": works}
    return render(request, "home_site/portfolio.html", context)
