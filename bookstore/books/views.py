from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .serializers import BookSerializer
from .models import Book

# Create your views here.


def index_page(request):
    return render(request, template_name='base.html')


class BookListAPIView(generics.ListCreateAPIView):
    """
    API endpoint that allows books to be viewed or created.
    """
    queryset = Book.objects.all()   # type: ignore
    serializer_class = BookSerializer


class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows users to be viewed, edited or deleted.
    """
    queryset = Book.objects.all()   # type: ignore
    serializer_class = BookSerializer
    lookup_field = 'pk'


class BooksQuerying(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['id', 'title', 'authors', 'acquired', 'publication_date', 'thumbnail']

    def get_queryset(self):
        return Book.objects.filter()    # type: ignore
