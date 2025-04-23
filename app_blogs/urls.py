from django.urls import path
from .views import BlogHomeView, BlogListView, BlogDetailView

app_name = "app_blogs"

urlpatterns = [
    path('', BlogHomeView.as_view(), name='home'),
    path('blogs_list/', BlogListView.as_view(), name='blog_list'),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
]
