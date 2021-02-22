from django.contrib import admin
from django.urls import path
from . import views

app_name = "book"

urlpatterns = [
    path('detail/<str:isbn13>/', views.detail, name="detail"), 
]
