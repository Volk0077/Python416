from django.shortcuts import render, get_object_or_404
from .models import Blog


def blog_view(request):
    blog = Blog.objects.order_by("-date")
    context = {"title": "Блог", "blog": blog}
    return render(request, "blog/blog.html", context)


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, "blog/details.html", {"bg": blog})