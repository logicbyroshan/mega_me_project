from django.urls import path
from . import HomeView, SkillListView, ProjectListView, ProjectDetailView, ExperienceListView,  ExperienceDetailView, FAQListView, ContactView, SubscribeView, TermsView, PrivacyView 

# URL Patterns
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('', SkillListView.as_view(), name='skill_list'),
    path('', ProjectListView.as_view(), name='project_list'),
    path('', ProjectDetailView.as_view(), name='project_detail'),
    path('', ExperienceListView.as_view(), name='experience_list'),
    path('', ExperienceDetailView.as_view(), name='experience_detail'),
    path('', FAQListView.as_view(), name='faq_list'),
    path('', ContactView.as_view(), name='contact'),
    path('', SubscribeView.as_view(), name='subscribe'),
    path('', TermsView.as_view(), name='terms'),
    path('', PrivacyView.as_view(), name='privacy'),
]
