from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, FormView
from .models import Skill, Project, Experience, FAQ  # Import models
from .forms import SubscriptionForm  # Ensure this form exists

# Home page
class HomeView(TemplateView):
    template_name = "app_portfolio/index.html"

# Skill list
class SkillListView(ListView):
    model = Skill
    template_name = "app_portfolio/skill_list.html"
    context_object_name = "skills"

# Project list
class ProjectListView(ListView):
    model = Project
    template_name = "app_portfolio/project_list.html"
    context_object_name = "projects"

# Project details
class ProjectDetailView(DetailView):
    model = Project
    template_name = "app_portfolio/project_detail.html"
    context_object_name = "project"

# Experience list
class ExperienceListView(ListView):
    model = Experience
    template_name = "app_portfolio/experience_list.html"
    context_object_name = "experiences"

# Experience details
class ExperienceDetailView(DetailView):
    model = Experience
    template_name = "app_portfolio/experience_detail.html"
    context_object_name = "experience"

# FAQ list
class FAQListView(ListView):
    model = FAQ
    template_name = "faq_list.html"
    context_object_name = "faqs"

# Contact page
class ContactView(TemplateView):
    template_name = "app_portfolio/contact.html"

# Subscription form
class SubscribeView(FormView):
    template_name = "app_portfolio/subscribe.html"
    form_class = SubscriptionForm
    success_url = "/thank-you/"

    def form_valid(self, form):
        form.save()  # Save the form data
        return HttpResponse("Thank you for subscribing!")

# Terms page
class TermsView(TemplateView):
    template_name = "app_portfolio/terms.html"

# Privacy page
class PrivacyView(TemplateView):
    template_name = "app_portfolio/privacy.html"
