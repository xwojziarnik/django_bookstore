from rest_framework import generics
from .serializers import BookSerializer
from .models import Book

# Create your views here.


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
