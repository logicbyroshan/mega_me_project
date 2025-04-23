from django.urls import path
from .views import (
    HelpHomeView, HelpContentListView, FAQListView,
    HelpContentDetailView, CourseDetailView, SessionDetailView
)

app_name = "app_help"

urlpatterns = [
    path('', HelpHomeView.as_view(), name='home'),
    path('contents/', HelpContentListView.as_view(), name='content_list'),
    path('faqs/', FAQListView.as_view(), name='faq_list'),

    path('contents/<int:pk>/', HelpContentDetailView.as_view(), name='content_detail'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('sessions/<int:pk>/', SessionDetailView.as_view(), name='session_detail'),
]
