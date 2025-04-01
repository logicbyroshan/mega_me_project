from django.urls import path
from .views import (
    HomeView, BlogListView, SubscribeView, BlogDetailView, RegisterView, 
    LoginView, LogoutView, ProfileView, ContactView, AuthorView, 
    TermsView, PrivacyView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blogs/', BlogListView.as_view(), name='blog_list'),
    path('blogs/<int:blog_id>/', BlogDetailView.as_view(), name='blog_detail'),
    path('subscribe/', SubscribeView.as_view(), name='subscribe'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('author/', AuthorView.as_view(), name='author'),
    path('terms/', TermsView.as_view(), name='terms'),
    path('privacy/', PrivacyView.as_view(), name='privacy'),
]
