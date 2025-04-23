from django.urls import path
from .views import (
    PortfolioHomeView, ExperienceListView, ProjectListView, SkillListView,
    ExperienceDetailView, ProjectDetailView
)

app_name = "app_portfolio"

urlpatterns = [
    path('', PortfolioHomeView.as_view(), name='home'),
    path('experiences/', ExperienceListView.as_view(), name='experience_list'),
    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('skills/', SkillListView.as_view(), name='skill_list'),

    path('experiences/<int:pk>/', ExperienceDetailView.as_view(), name='experience_detail'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
]
