from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse, HttpResponseRedirect
import requests
from .models import Bookmark
from django.db import connection
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from search.models import SearchTable

def index(request):

    #---------> IMPORTANT: This API link (https://api.itbook.store/1.0/) gave me 404 error. Thats why, I used new books API. <---------


    #-------------------------------------------------------SORRY ABOUT THAT :(-------------------------------------------------------
    #I can't used elasticsearch with API. I researched this for 2 days but it didn't worked without model. Thats why, I created a model for search engine,
    #and saved some data to this model from API. This part will only work first time. I will learn the truth way of this in the shortest time.
    data = SearchTable.objects.all()
    if not data: #If there is no data on our table, it works.
        url = requests.get("https://api.itbook.store/1.0/new").json()
        books = url["books"]
            
        for i in range(0, len(books)):
            details = requests.get("https://api.itbook.store/1.0/books/" + books[i]["isbn13"]).json()

            add_to_table = SearchTable(title = details["title"], author = details["authors"], isbn13 = details["isbn13"], image = details["image"], keyword = (details["title"] + " " + details["authors"] + " " + details["isbn13"]))
            add_to_table.save()
    #-------------------------------------------------------SORRY ABOUT THAT :(-------------------------------------------------------

    response = requests.get("https://api.itbook.store/1.0/new").json() #Books API
    books = response["books"]

    if request.user.is_authenticated:
        #Check the color of bookmark button.
        username = request.user.username
        get_data_on_table = Bookmark.objects.filter(username = username)

        if get_data_on_table:
            button_status = list() 
            result = list()
            for i in range(0, len(get_data_on_table)):
                button_status.append(requests.get("https://api.itbook.store/1.0/books/" + get_data_on_table[i].book_code).json())

            for i in range(0, len(books)):
                for j in range(0, len(button_status)):
                    t_or_f = False
                    if(button_status[j]["isbn13"] == books[i]["isbn13"]):
                        t_or_f = True 
                        break   
                result.append(t_or_f) #If book in our list, result is true, button is red.

            for i in range(0, len(books)):
                books[i]["result"] = result[i] #Added results on our list.

    return render(request, "index.html", {"books": books})





def detail(request, isbn13):

    details = requests.get("https://api.itbook.store/1.0/books/" + isbn13).json() #SEARCH API

    if request.user.is_authenticated:
        #Check the color of bookmark button again.
        username = request.user.username
        get_data_on_table = Bookmark.objects.filter(username = username)

        if get_data_on_table:
            button_status = list() 
            result = list()
            for i in range(0, len(get_data_on_table)):
                button_status.append(requests.get("https://api.itbook.store/1.0/books/" + get_data_on_table[i].book_code).json())

            for i in range(0, len(details)):
                for j in range(0, len(button_status)):
                    t_or_f = False
                    if(button_status[j]["isbn13"] == details["isbn13"]):
                        t_or_f = True 
                        break   
                result.append(t_or_f)

            for i in range(0, len(details)):
                details["result"] = result[i]
    
    return render(request, "detail.html", {"details": details})



@login_required
def bookmark_check(request, isbn13, id):  #If we click a add-remove bookmark button, this function will update our bookmark table.
    username = request.user.username
    isbn13 = isbn13
    check_on_table = Bookmark.objects.filter(username = username)
    for i in range(0, len(check_on_table)):
        if check_on_table[i].book_code == isbn13:
            Bookmark.objects.filter(id = check_on_table[i].id).delete() #Data deleted our table.
            messages.info(request,"Book Removed On Your Bookmark List.") 
            return HttpResponseRedirect(request.META.get('HTTP_REFERER')) #We go back to the same page.

    add_to_table = Bookmark(username = username, book_code = isbn13)
    add_to_table.save() #Data added our table
    messages.info(request,"Book Added On Your Bookmark List.")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER')) #We go back to the same page.