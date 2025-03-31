from django.shortcuts import render

# Home Page
def home(request):
    return render(request, 'home.html')

# About Page
def about(request):
    return render(request, 'about.html')

# Contact Page
def contact(request):
    return render(request, 'contact.html')

# Ventures
def ventures(request):
    return render(request, 'ventures.html')

def venture_detail(request, venture_id):
    return render(request, 'venture_detail.html', {'venture_id': venture_id})

# Feedback
def feedback(request):
    return render(request, 'feedback.html')

def feedback_thank_you(request):
    return render(request, 'feedback_thank_you.html')

def submit_feedback(request):
    if request.method == 'POST':
        # Process feedback submission (Save to DB, Send email, etc.)
        return render(request, 'feedback_thank_you.html')
    return render(request, 'feedback.html')
