from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('aboutme/', views.aboutme, name='aboutme'),
    path('photos/', views.photos, name='photos'),
    path('photos/<int:photo_id>/', views.photo_detail, name='photo_detail'),
    path('certificates/', views.certificates, name='certificates'),
    path('certificates/<int:certificate_id>/', views.certificate_detail, name='certificate_detail'),
    path('achievements/', views.achievements, name='achievements'),
    path('achievements/<int:achievement_id>/', views.achievement_detail, name='achievement_detail'),
    path('problems/', views.problems, name='problems'),
    path('problems/<int:problem_id>/', views.problem_detail, name='problem_detail'),
    path('education/', views.education, name='education'),
    path('education/<int:education_id>/', views.education_detail, name='education_detail'),
    path('social/', views.social, name='social'),
    path('social/<int:social_id>/', views.social_detail, name='social_detail'),
]
