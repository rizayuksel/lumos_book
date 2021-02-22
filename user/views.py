from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from book.models import Bookmark
import requests



def sign_up(request):
    form = RegisterForm(request.POST or None)
    if (form.is_valid()): 
        first_name = form.cleaned_data.get("first_name")
        last_name = form.cleaned_data.get("last_name")
        email = form.cleaned_data.get("email")
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username=username, first_name=first_name, last_name=last_name, email=email)
        newUser.set_password(password)
        newUser.save()  #New user saved our database
        login(request, newUser) #For auto login
        messages.info(request, "Successful")
        return redirect("index")
    context = {
        "form": form
    }
    return render(request, "register.html", context)


def login_user(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    if (form.is_valid()):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if (user is None): # Check the datas on our database
            messages.info(request, "Wrong Username or Password")
            return render(request, "login.html", context)

        messages.info(request, "Welcome ")
        login(request, user)
        return redirect("index")

    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    messages.info(request, "Good Bye.")
    return redirect("index")

def user_profile(request): #List bookmarks.
    username = request.user.username
    get_data_on_table = Bookmark.objects.filter(username = username)
    details = list()
    for i in range(0, len(get_data_on_table)):
        details.append(requests.get("https://api.itbook.store/1.0/books/" + get_data_on_table[i].book_code).json())

    return render(request, "profile.html", {"details": details})