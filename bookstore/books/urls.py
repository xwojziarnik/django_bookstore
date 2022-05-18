from django.urls import path, include
from rest_framework import routers, urls

from . import views

router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)


urlpatterns = [
    # path('', views.index, name='index'),
    # path('book-search/', views.book_search, name='book_search'),
    path('', include(routers.urls))
]
