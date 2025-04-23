from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import get_object_or_404
from .models import Blog  # assuming your blog model is named 'Blog'

# Home Page View
class BlogHomeView(TemplateView):
    template_name = "blogs_app/blog_home.html"

# Blog List View
class BlogListView(ListView):
    model = Blog
    template_name = "blogs_app/blog_list.html"
    context_object_name = "blogs"

# Blog Detail View
class BlogDetailView(DetailView):
    model = Blog
    template_name = "blogs_app/blog_dtl.html"
    context_object_name = "blog"
