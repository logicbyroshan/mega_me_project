from django.views.generic import TemplateView, ListView
from .models import Achievement, Education, Mention, Photo, Problem

# Home View
class PersonalHomeView(TemplateView):
    template_name = "personal_app/personal_home.html"

# Achievements List View
class AchievementListView(ListView):
    model = Achievement
    template_name = "personal_app/personal_achievement_list.html"
    context_object_name = "achievements"

# Education List View
class EducationListView(ListView):
    model = Education
    template_name = "personal_app/personal_education_list.html"
    context_object_name = "educations"

# Mentions List View
class MentionListView(ListView):
    model = Mention
    template_name = "personal_app/personal_mention_list.html"
    context_object_name = "mentions"

# Photos List View
class PhotoListView(ListView):
    model = Photo
    template_name = "personal_app/personal_photo_list.html"
    context_object_name = "photos"

# Problems List View
class ProblemListView(ListView):
    model = Problem
    template_name = "personal_app/personal_problem_list.html"
    context_object_name = "problems"
