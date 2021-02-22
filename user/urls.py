from django.contrib import admin
from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path("signup/", views.sign_up, name="register"),
    path("login/", views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('profile/', views.user_profile, name="profile"),
]
