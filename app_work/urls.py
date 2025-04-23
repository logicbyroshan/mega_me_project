from django.urls import path
from .views import WorkHomeView, ServiceDetailView

app_name = "app_work"

urlpatterns = [
    path('', WorkHomeView.as_view(), name='home'),
    path('services/<int:pk>/', ServiceDetailView.as_view(), name='service_detail'),
]
