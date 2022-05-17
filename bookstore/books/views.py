from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("Hello! You are at the books index page.")


def book_search(request):
    search_text = request.GET.get("search", "")
    return render(request, "book_search.html", {"search_text": search_text})
