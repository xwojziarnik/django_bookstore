from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_page),
    path('books/', views.BookListAPIView.as_view()),
    path('books/<int:pk>/', views.BookDetailAPIView.as_view()),
    path('books/search/', views.BooksQuerying.as_view())
]
