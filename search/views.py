from django.shortcuts import render
from search.documents import SearchBookDocument
from book.models import Bookmark
import requests

def search(request):
    keyword = request.GET.get("keyword") #Frontend send us a keyword.
    if keyword:
        books = SearchBookDocument.search().query("match", keyword = keyword) #Elasticsearch search this keyword on own data set.
    return render(request, "search.html", {"books": books}) #Send the results.