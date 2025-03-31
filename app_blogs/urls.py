from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog_list/', views.blog_list, name='blog_list'),
    path('blogs/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('/search/', views.search, name='search'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('blogs/<int:blog_id>/like/', views.like_blog, name='like_blog'),
    path('blogs/<int:blog_id>/comment/', views.comment, name='comment'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('password_reset/', views.password_reset, name='password_reset'),
    path('password_reset/done/', views.password_reset_done, name='password_reset_done'),
    path('password_change/', views.password_change, name='password_change'),
    path('password_change/done/', views.password_change_done, name='password_change_done'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    
]
