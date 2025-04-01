from django.shortcuts import render
from django.contrib.auth.forms import SubscriptionForm
from django.http import HttpResponse
from django.views import view, viewList 


# Views
class HomeView(view):
    def get(self, request):
        return render(request, 'home.html')

class SkillListView(viewList):
    def get(self, request):
        skills = Skill.objects.all()
        return render(request, 'skill_list.html', {'skills': skills})

class ProjectListView(viewList):
    def get(self, request):
        projects = Project.objects.all()
        return render(request, 'project_list.html', {'projects': projects})

class ProjectDetailView(viewList):
    def get(self, request, project_id):
        project = Project.objects.get(id=project_id)
        return render(request, 'project_detail.html', {'project': project})

class ExperienceListView(viewList):
    def get(self, request):
        experiences = Experience.objects.all()
        return render(request, 'experience_list.html', {'experiences': experiences})

class ExperienceDetailView(view):
    def get(self, request, experience_id):
        experience = Experience.objects.get(id=experience_id)
        return render(request, 'experience_detail.html', {'experience': experience})

class FAQListView(viewList):
    def get(self, request):
        faqs = FAQ.objects.all()
        return render(request, 'faq_list.html', {'faqs': faqs})

class ContactView(view):
    def get(self, request):
        return render(request, 'contact.html')

class SubscribeView(view):
    def get(self, request):
        form = SubscriptionForm()
        return render(request, 'subscribe.html', {'form': form})

    def post(self, request):
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Thank you for subscribing!")
        return render(request, 'subscribe.html', {'form': form})

class TermsView(view):
    def get(self, request):
        return render(request, 'terms.html')

class PrivacyView(view):
    def get(self, request):
        return render(request, 'privacy.html')
