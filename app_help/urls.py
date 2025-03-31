from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
    path('support/', views.support, name='support'),
    path('feedback/', views.feedback, name='feedback'),
    path('faq_list/', views.faq_list, name='faq_list'),
    path('course/', views.course, name='course'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('course/<int:course_id>/enroll/', views.enroll, name='enroll'),
    path('mentorship/', views.mentorship, name='mentorship'),
    path('mentorship/<int:mentorship_id>/', views.mentorship_detail, name='mentorship_detail'),
    path('mentorship/<int:mentorship_id>/apply/', views.apply_mentorship, name='apply_mentorship'),
    path('mentorship/<int:mentorship_id>/schedule/', views.schedule_mentorship, name='schedule_mentorship'),
    path('mentorship/<int:mentorship_id>/feedback/', views.mentorship_feedback, name='mentorship_feedback'),
    path('mentorship/<int:mentorship_id>/resources/', views.mentorship_resources, name='mentorship_resources'),
    path('resources/', views.resources, name='resources'),
    path('resources/<int:resource_id>/', views.resource_detail, name='resource_detail'),
    path('resources/<int:resource_id>/download/', views.download_resource, name='download_resource'),
    path('resources/<int:resource_id>/share/', views.share_resource, name='share_resource'),
    path('resources/<int:resource_id>/comment/', views.comment_resource, name='comment_resource'),
    path('resources/<int:resource_id>/like/', views.like_resource, name='like_resource'),
]
