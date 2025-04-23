from django.urls import path
from .views import HobbyHomeView, BookListView, PoemListView, ProductListView

app_name = "app_hobby"

urlpatterns = [
    path('', HobbyHomeView.as_view(), name='home'),
    path('books/', BookListView.as_view(), name='book_list'),
    path('poems/', PoemListView.as_view(), name='poem_list'),
    path('products/', ProductListView.as_view(), name='product_list'),
]
