from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Blog, Comment, Profile

# Home Page
def home(request):
    return render(request, 'blog/home.html')

# List all blogs
def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blog_list.html', {'blogs': blogs})

# Blog detail view
def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    comments = Comment.objects.filter(blog=blog)
    return render(request, 'blog/blog_detail.html', {'blog': blog, 'comments': comments})

# Search functionality
def search(request):
    query = request.GET.get('q')
    results = Blog.objects.filter(title__icontains=query) if query else []
    return render(request, 'blog/search_results.html', {'results': results, 'query': query})

# About Page
def about(request):
    return render(request, 'blog/about.html')

# Contact Page
def contact(request):
    return render(request, 'blog/contact.html')

# Subscribe functionality
def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # Add email to your subscription list (not implemented)
        return JsonResponse({'message': 'Subscribed successfully!'})
    return render(request, 'blog/subscribe.html')

# Like a blog
@login_required
def like_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.user in blog.likes.all():
        blog.likes.remove(request.user)  # Unlike
        liked = False
    else:
        blog.likes.add(request.user)  # Like
        liked = True
    return JsonResponse({'liked': liked, 'like_count': blog.likes.count()})

# Comment on a blog
@login_required
def comment(request, blog_id):
    if request.method == 'POST':
        blog = get_object_or_404(Blog, id=blog_id)
        content = request.POST.get('content')
        Comment.objects.create(user=request.user, blog=blog, content=content)
        return redirect('blog_detail', blog_id=blog_id)
    return redirect('home')

# Register new users
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

# Login users
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

# Logout users
def logout_view(request):
    logout(request)
    return redirect('home')

# Password reset view
def password_reset(request):
    form = PasswordResetForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save(request=request)
        return redirect('password_reset_done')
    return render(request, 'users/password_reset.html', {'form': form})

# Password reset done view
def password_reset_done(request):
    return render(request, 'users/password_reset_done.html')

# Password change view
@login_required
def password_change(request):
    form = PasswordChangeForm(user=request.user, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('password_change_done')
    return render(request, 'users/password_change.html', {'form': form})

# Password change done view
def password_change_done(request):
    return render(request, 'users/password_change_done.html')

# User Profile
@login_required
def profile(request):
    user_profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'users/profile.html', {'profile': user_profile})

# Edit User Profile
@login_required
def edit_profile(request):
    if request.method == 'POST':
        user = request.user
        user.username = request.POST.get('username', user.username)
        user.email = request.POST.get('email', user.email)
        user.save()
        return redirect('profile')
    return render(request, 'users/edit_profile.html')
