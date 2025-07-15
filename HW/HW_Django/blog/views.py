from django.shortcuts import render
from .models import Blog


def blog_view(request):
    blog = Blog.objects.all()
    context = {"title": "Блог", "blog": blog}
    return render(request, "blog/blog.html", context)
