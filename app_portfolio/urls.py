from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    path('experience/', views.experience, name='experience'),
    path('experience/<int:experience_id>/', views.experience_detail, name='experience_detail'),
    path('skills/', views.skills, name='skills'),
    path('contact/', views.contact, name='contact'),
]
