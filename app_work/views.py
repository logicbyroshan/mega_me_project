from django.shortcuts import render, redirect

# Home Page
def home(request):
    return render(request, 'home.html')

# Work Listings
def work_list(request):
    return render(request, 'work_list.html')

def work_detail(request, work_id):
    return render(request, 'work_detail.html', {'work_id': work_id})

# Search
def search(request):
    query = request.GET.get('q', '')
    return render(request, 'search_results.html', {'query': query})

# About and Contact Pages
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

# Ordering Work
def order_work(request):
    if request.method == 'POST':
        # Handle work ordering logic here
        return redirect('work_list')
    return render(request, 'order_work.html')

# Like and Comment
def like_work(request, work_id):
    return redirect('work_detail', work_id=work_id)

def comment(request, work_id):
    if request.method == 'POST':
        # Handle comment logic here
        return redirect('work_detail', work_id=work_id)
    return render(request, 'comment_form.html', {'work_id': work_id})

# Authentication
def register(request):
    return render(request, 'register.html')

def login_view(request):
    return render(request, 'login.html')

def logout_view(request):
    return redirect('home')

# Password Reset & Change
def password_reset(request):
    return render(request, 'password_reset.html')

def password_reset_done(request):
    return render(request, 'password_reset_done.html')

def password_change(request):
    return render(request, 'password_change.html')

def password_change_done(request):
    return render(request, 'password_change_done.html')

# User Profile
def profile(request):
    return render(request, 'profile.html')

def edit_profile(request):
    return render(request, 'edit_profile.html')

def profile_work_list(request):
    return render(request, 'profile_work_list.html')
