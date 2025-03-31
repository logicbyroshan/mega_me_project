from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('ventures/', views.ventures, name='ventures'),
    path('ventures/<int:venture_id>/', views.venture_detail, name='venture_detail'),
    path('feedback/', views.feedback, name='feedback'),
    path('feedback/thank-you/', views.feedback_thank_you, name='feedback_thank_you'),
    path('feedback/submit/', views.submit_feedback, name='submit_feedback'),
]
