from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # Auth (регистрация и авторизация)
    path("signup/", views.signup_user, name="signupuser"),
    path("logout/", views.logout_user, name="logoutuser"),
    path("login/", views.login_user, name="loginuser"),
    
    # Todos (постановка задач)
    path("current/", views.current_todos, name="currenttodos"),
    path("", views.home, name="home"),
    path("create/", views.create_todo, name="createtodo"),
    path("todo/<int:todo_pk>/", views.view_todo, name="viewtodo"),
]
