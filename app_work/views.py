from django.views.generic import TemplateView, DetailView
from .models import Service

# Work Home View
class WorkHomeView(TemplateView):
    template_name = "work_app/freelance_home.html"

# Service Detail View
class ServiceDetailView(DetailView):
    model = Service
    template_name = "work_app/freelance_service_dtl.html"
    context_object_name = "service"
