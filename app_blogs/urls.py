from django.urls import path
from views import HomeView, BlogListView, SubscribeView, BlogDetailView, RegisterView, LoginView, LogoutView, ProfileView, ContactView, AuthorView, TermsView, PrivacyView 

urlpatterns = [
     path('', HomeView.as_view(), name='home'),
    path('', BlogListView.as_view(), name='blog_list'),
    path('', BlogDetailView.as_view(), name='blog_detail'),
    path('', SubscribeView.as_view(), name='subscribe'),
    path('', RegisterView.as_view(), name='register'),
    path('', LoginView.as_view(), name='login'),
    path('', LogoutView.as_view(), name='logout'),
    path('', ProfileView.as_view(), name='profile'),
    path('', ContactView.as_view(), name='contact'),
    path('', AuthorView.as_view(), name='author'),
    path('', TermsView.as_view(), name='terms'),
    path('', PrivacyView.as_view(), name='privacy'),
]
