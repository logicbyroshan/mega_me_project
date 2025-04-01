from django.urls import path
from .views import (
    HomeView, SkillListView, ProjectListView, ProjectDetailView,
    ExperienceListView, ExperienceDetailView, FAQListView, ContactView,
    SubscribeView, TermsView, PrivacyView
)

# URL Patterns
urlpatterns = [
    path('', HomeView.as_view(), name='home'),  # Home Page
    path('skills/', SkillListView.as_view(), name='skill_list'),  # Skills List
    path('projects/', ProjectListView.as_view(), name='project_list'),  # Projects List
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),  # Project Details
    path('experiences/', ExperienceListView.as_view(), name='experience_list'),  # Experiences List
    path('experiences/<int:pk>/', ExperienceDetailView.as_view(), name='experience_detail'),  # Experience Details
    path('faq/', FAQListView.as_view(), name='faq_list'),  # FAQs List
    path('contact/', ContactView.as_view(), name='contact'),  # Contact Page
    path('subscribe/', SubscribeView.as_view(), name='subscribe'),  # Subscription Page
    path('terms/', TermsView.as_view(), name='terms'),  # Terms & Conditions
    path('privacy/', PrivacyView.as_view(), name='privacy'),  # Privacy Policy
]
