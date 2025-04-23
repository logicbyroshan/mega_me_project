from django.views.generic import TemplateView, DetailView
from .models import Startup

# Home View
class VentureHomeView(TemplateView):
    template_name = "venture_app/startup_home.html"

# Startup Detail View
class StartupDetailView(DetailView):
    model = Startup
    template_name = "venture_app/startup_dtl.html"
    context_object_name = "startup"

# Idea Detail View
class IdeaDetailView(DetailView):
    model = Startup
    template_name = "venture_app/startup_dtl.html"
    context_object_name = "idea"
