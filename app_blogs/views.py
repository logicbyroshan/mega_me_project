from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm, SubscriptionForm, RegistrationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.views import view, ViewList



class HomeView(view):
    def get(self, request):
        return render(request, 'home.html')

class BlogListView(ViewList):
    def get(self, request):
        blogs = Blog.objects.all()
        return render(request, 'blog_list.html', {'blogs': blogs})
    
class BlogDetailView(view):
    def get(self, request, blog_id):
        blog = Blog.objects.get(id=blog_id)
        return render(request, 'blog_detail.html', {'blog': blog})

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
    
class RegisterView(view):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
        return render(request, 'register.html', {'form': form})

class LoginView(view):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        return HttpResponse("Invalid credentials!")

class LogoutView(view):
    def get(self, request):
        logout(request)
        return redirect('home')

class ProfileView(view):
    def get(self, request):
        return render(request, 'profile.html')

class ContactView(view):
    def get(self, request):
        return render(request, 'contact.html')

class AuthorView(view):
    def get(self, request):
        return render(request, 'author.html')

class TermsView(view):
    def get(self, request):
        return render(request, 'terms.html')

class PrivacyView(view):
    def get(self, request):
        return render(request, 'privacy.html')
