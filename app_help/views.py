from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Course, Mentorship, Resource, FAQ, Feedback

# Home Page
def home(request):
    return render(request, 'home.html')

# Static Pages
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def faq(request):
    return render(request, 'faq.html')

def terms(request):
    return render(request, 'terms.html')

def privacy(request):
    return render(request, 'privacy.html')

def support(request):
    return render(request, 'support.html')

# Feedback Form
def feedback(request):
    if request.method == 'POST':
        user_feedback = request.POST.get('feedback')
        Feedback.objects.create(user=request.user, content=user_feedback)
        return JsonResponse({'message': 'Feedback submitted successfully!'})
    return render(request, 'feedback.html')

# List of FAQs
def faq_list(request):
    faqs = FAQ.objects.all()
    return render(request, 'faq_list.html', {'faqs': faqs})

# Course Listing
def course(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})

# Course Detail View
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'course_detail.html', {'course': course})

# Enroll in a Course
@login_required
def enroll(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    course.students.add(request.user)
    return JsonResponse({'message': f'Enrolled in {course.title} successfully!'})

# Mentorship Program Listing
def mentorship(request):
    mentorships = Mentorship.objects.all()
    return render(request, 'mentorship.html', {'mentorships': mentorships})

# Mentorship Detail View
def mentorship_detail(request, mentorship_id):
    mentorship = get_object_or_404(Mentorship, id=mentorship_id)
    return render(request, 'mentorship_detail.html', {'mentorship': mentorship})

# Apply for Mentorship
@login_required
def apply_mentorship(request, mentorship_id):
    mentorship = get_object_or_404(Mentorship, id=mentorship_id)
    mentorship.applicants.add(request.user)
    return JsonResponse({'message': 'Mentorship application submitted successfully!'})

# Schedule a Mentorship Session
@login_required
def schedule_mentorship(request, mentorship_id):
    mentorship = get_object_or_404(Mentorship, id=mentorship_id)
    return render(request, 'schedule_mentorship.html', {'mentorship': mentorship})

# Submit Feedback for Mentorship
@login_required
def mentorship_feedback(request, mentorship_id):
    if request.method == 'POST':
        mentorship = get_object_or_404(Mentorship, id=mentorship_id)
        feedback_text = request.POST.get('feedback')
        Feedback.objects.create(user=request.user, mentorship=mentorship, content=feedback_text)
        return JsonResponse({'message': 'Feedback submitted successfully!'})
    return redirect('mentorship_detail', mentorship_id=mentorship_id)

# Resources Page
def resources(request):
    resources = Resource.objects.all()
    return render(request, 'resources.html', {'resources': resources})

# Resource Detail View
def resource_detail(request, resource_id):
    resource = get_object_or_404(Resource, id=resource_id)
    return render(request, 'resource_detail.html', {'resource': resource})

# Download a Resource
@login_required
def download_resource(request, resource_id):
    resource = get_object_or_404(Resource, id=resource_id)
    response = HttpResponse(resource.file, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{resource.file.name}"'
    return response

# Share a Resource
@login_required
def share_resource(request, resource_id):
    resource = get_object_or_404(Resource, id=resource_id)
    return JsonResponse({'message': f'Shared {resource.title} successfully!'})

# Comment on a Resource
@login_required
def comment_resource(request, resource_id):
    if request.method == 'POST':
        resource = get_object_or_404(Resource, id=resource_id)
        content = request.POST.get('content')
        resource.comments.create(user=request.user, content=content)
        return redirect('resource_detail', resource_id=resource_id)
    return redirect('resources')

# Like a Resource
@login_required
def like_resource(request, resource_id):
    resource = get_object_or_404(Resource, id=resource_id)
    if request.user in resource.likes.all():
        resource.likes.remove(request.user)  # Unlike
        liked = False
    else:
        resource.likes.add(request.user)  # Like
        liked = True
    return JsonResponse({'liked': liked, 'like_count': resource.likes.count()})
