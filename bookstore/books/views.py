import json
from django.http import HttpResponse, JsonResponse
from django.core.handlers.wsgi import WSGIRequest
from rest_framework import viewsets

from .models import Book

# Create your views here.
from .serializers import BookSerializer


def index(request: WSGIRequest) -> HttpResponse:

    books = Book.objects.all() #TypeError: Object of type QuerySet is not JSON serializable
    return HttpResponse(json.dumps(books))


def book_search(request: WSGIRequest) -> JsonResponse:
    search_text = request.GET.get("search", "")
    return JsonResponse({"Books": search_text})

class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
