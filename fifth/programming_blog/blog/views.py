from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from .models import *


menu = [
    {'title':'Добавить статью', 'url_name': 'index'},
    {'title':'Войти', 'url_name': 'index'},
]


class BlogHome(ListView):
    model = Blog
    template_name = "blog/index.html"
    context_object_name = "posts"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Главная страница"
        context['cat_selected'] = 0
        context['menu'] = mu= menu
        return context
    
    def get_queryset(self):
        return Blog.objects.filter(is_published=True).selected_related('cat')


class ShowPost(DeleteView):
    model = Blog
    template_name = "blog/post.html"
    slug_url_kwarg = "post_slug"
    context_object_name = "post"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['menu'] = mu= menu
        return context
    

class BlogCategory(ListView):
    model = Blog
    template_name = "blog/index.html"
    context_object_name = "posts"