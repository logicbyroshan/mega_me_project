from django.urls import path
from .views import VentureHomeView, StartupDetailView, IdeaDetailView

app_name = "app_venture"

urlpatterns = [
    path('', VentureHomeView.as_view(), name='home'),
    path('startups/<int:pk>/', StartupDetailView.as_view(), name='startup_detail'),
    path('ideas/<int:pk>/', IdeaDetailView.as_view(), name='idea_detail'),
]
