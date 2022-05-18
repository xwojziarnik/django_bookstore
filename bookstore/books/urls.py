from django.urls import path

from . import views

urlpatterns = [
    path('', views.BookListAPIView.as_view()),
    path('books/<int:pk>/', views.BookDetailAPIView.as_view())
]
