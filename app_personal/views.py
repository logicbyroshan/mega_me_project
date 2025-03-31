from django.shortcuts import render, get_object_or_404

# Home Page
def home(request):
    return render(request, 'home.html')

# About Me
def aboutme(request):
    return render(request, 'aboutme.html')

# Photos
def photos(request):
    return render(request, 'photos.html')

def photo_detail(request, photo_id):
    return render(request, 'photo_detail.html', {'photo_id': photo_id})

# Certificates
def certificates(request):
    return render(request, 'certificates.html')

def certificate_detail(request, certificate_id):
    return render(request, 'certificate_detail.html', {'certificate_id': certificate_id})

# Achievements
def achievements(request):
    return render(request, 'achievements.html')

def achievement_detail(request, achievement_id):
    return render(request, 'achievement_detail.html', {'achievement_id': achievement_id})

# Problems
def problems(request):
    return render(request, 'problems.html')

def problem_detail(request, problem_id):
    return render(request, 'problem_detail.html', {'problem_id': problem_id})

# Education
def education(request):
    return render(request, 'education.html')

def education_detail(request, education_id):
    return render(request, 'education_detail.html', {'education_id': education_id})

# Social
def social(request):
    return render(request, 'social.html')

def social_detail(request, social_id):
    return render(request, 'social_detail.html', {'social_id': social_id})
