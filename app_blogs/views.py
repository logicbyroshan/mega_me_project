from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views import View
from .models import Blog 
# Home View
class HomeView(View):
    def get(self, request):
        return render(request, 'app_blogs/home.html')

# Blog Views
class BlogListView(View):
    def get(self, request):
        blogs = Blog.objects.all()
        return render(request, 'app_blogs/blog_list.html', {'blogs': blogs})
    
class BlogDetailView(View):
    def get(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        return render(request, 'app_blogs/blog_detail.html', {'blog': blog})


# Profile View
class ProfileView(View):
    @login_required
    def get(self, request):
        return render(request, 'profile.html')

# Static Page Views
class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')
