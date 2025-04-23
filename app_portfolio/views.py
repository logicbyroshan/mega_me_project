from django.views.generic import TemplateView, ListView, DetailView
from .models import Experience, Project, Skill

# Portfolio Home View
class PortfolioHomeView(TemplateView):
    template_name = "portfolio_app/portfolio_home.html"

# Experience List View
class ExperienceListView(ListView):
    model = Experience
    template_name = "portfolio_app/portfolio_experience_list.html"
    context_object_name = "experiences"

# Project List View
class ProjectListView(ListView):
    model = Project
    template_name = "portfolio_app/portfolio_project_list.html"
    context_object_name = "projects"

# Skill List View
class SkillListView(ListView):
    model = Skill
    template_name = "portfolio_app/portfolio_skill_list.html"
    context_object_name = "skills"

# Experience Detail View
class ExperienceDetailView(DetailView):
    model = Experience
    template_name = "portfolio_app/portfolio_experience_dtl.html"
    context_object_name = "experience"

# Project Detail View
class ProjectDetailView(DetailView):
    model = Project
    template_name = "portfolio_app/portfolio_project_dtl.html"
    context_object_name = "project"
