from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from home_site import views
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("portfolio/", views.portfolio_view, name="portfolio"),
    path("blog/", include("blog.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
