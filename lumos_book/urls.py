from django.contrib import admin
from django.urls import path, include
from book import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('bookmark/<str:isbn13>/<int:id>/', views.bookmark_check, name = "bookmark"),
    path('book/', include("book.urls")), #The way of book urls.
    path('search/', include("search.urls")), #The way of search urls.
    path('user/', include("user.urls")), #The way of user urls.
]
