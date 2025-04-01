from django.urls import path
from .views import (
    HomeView, SkillListView, ProjectListView, ProjectDetailView,
    ExperienceListView, ExperienceDetailView, FAQListView, ContactView)

# URL Patterns
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('skills/', SkillListView.as_view(), name='skill_list'),
    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('experiences/', ExperienceListView.as_view(), name='experience_list'),
    path('experiences/<int:pk>/', ExperienceDetailView.as_view(), name='experience_detail'),
    path('faq/', FAQListView.as_view(), name='faq_list'),
    path('contact/', ContactView.as_view(), name='contact'),
]
