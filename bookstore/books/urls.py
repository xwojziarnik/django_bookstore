from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book-search/', views.book_search, name='book_search'),
]
