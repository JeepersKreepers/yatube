from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # path() для страницы регистрации нового пользователя
    # её полный адрес будет auth/signup/, но префикс auth/ обрабатывется в головном urls.py
    path("signup/", views.SignUp.as_view(), name="signup"),
]