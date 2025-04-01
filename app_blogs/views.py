from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.views import View
from .models import Blog  # Assuming Blog model exists
from .forms import SubscriptionForm, RegistrationForm  # Custom Forms

# Home View
class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

# Blog Views
class BlogListView(View):
    def get(self, request):
        blogs = Blog.objects.all()
        return render(request, 'blog_list.html', {'blogs': blogs})
    
class BlogDetailView(View):
    def get(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        return render(request, 'blog_detail.html', {'blog': blog})

# Subscription View
class SubscribeView(View):
    def get(self, request):
        form = SubscriptionForm()
        return render(request, 'subscribe.html', {'form': form})

    def post(self, request):
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Thank you for subscribing!")
        return render(request, 'subscribe.html', {'form': form})

# User Registration View
class RegisterView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Password hashing is automatic
            login(request, user)
            return redirect('profile')
        return render(request, 'register.html', {'form': form})

# User Login View
class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
        return render(request, 'login.html', {'form': form, 'error': "Invalid credentials!"})

# Logout View
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')

# Profile View
class ProfileView(View):
    @login_required
    def get(self, request):
        return render(request, 'profile.html')

# Static Page Views
class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')

class AuthorView(View):
    def get(self, request):
        return render(request, 'author.html')

class TermsView(View):
    def get(self, request):
        return render(request, 'terms.html')

class PrivacyView(View):
    def get(self, request):
        return render(request, 'privacy.html')
