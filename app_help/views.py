from django.views.generic import TemplateView, ListView, DetailView
from .models import Content, Course, Session
from core.models import FAQ

# Home View
class HelpHomeView(TemplateView):
    template_name = "help_app/help_home.html"

# Content List View
class HelpContentListView(ListView):
    model = Content
    template_name = "help_app/help_content_list.html"
    context_object_name = "contents"

# FAQs List View
class FAQListView(ListView):
    model = FAQ
    template_name = "help_app/help_faq_list.html"
    context_object_name = "faqs"

# Content Detail View
class HelpContentDetailView(DetailView):
    model = Content
    template_name = "help_app/help_content_dtl.html"
    context_object_name = "content"

# Course Detail View
class CourseDetailView(DetailView):
    model = Course
    template_name = "help_app/help_course_dtl.html"
    context_object_name = "course"

# Session Detail View
class SessionDetailView(DetailView):
    model = Session
    template_name = "help_app/help_session_dtl.html"
    context_object_name = "session"
