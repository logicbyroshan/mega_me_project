from django.urls import path
from .views import (
    PersonalHomeView, AchievementListView, EducationListView,
    MentionListView, PhotoListView, ProblemListView
)

app_name = "app_personal"

urlpatterns = [
    path('', PersonalHomeView.as_view(), name='home'),
    path('achievements/', AchievementListView.as_view(), name='achievement_list'),
    path('education/', EducationListView.as_view(), name='education_list'),
    path('mentions/', MentionListView.as_view(), name='mention_list'),
    path('photos/', PhotoListView.as_view(), name='photo_list'),
    path('problems/', ProblemListView.as_view(), name='problem_list'),
]
