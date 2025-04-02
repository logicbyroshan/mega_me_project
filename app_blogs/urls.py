from django.urls import path
from .views import (
    HomeView, BlogListView, BlogDetailView, ProfileView, ContactView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blogs/', BlogListView.as_view(), name='blog_list'),
    path('blogs/<int:blog_id>/', BlogDetailView.as_view(), name='blog_detail'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('contact/', ContactView.as_view(), name='contact'),

]
