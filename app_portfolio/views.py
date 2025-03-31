from django.shortcuts import render

# Home Page
def home(request):
    return render(request, 'home.html')

# Projects
def projects(request):
    return render(request, 'projects.html')

def project_detail(request, project_id):
    return render(request, 'project_detail.html', {'project_id': project_id})

# Experience
def experience(request):
    return render(request, 'experience.html')

def experience_detail(request, experience_id):
    return render(request, 'experience_detail.html', {'experience_id': experience_id})

# Skills
def skills(request):
    return render(request, 'skills.html')

# Contact
def contact(request):
    return render(request, 'contact.html')
