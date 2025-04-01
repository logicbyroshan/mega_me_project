from django.shortcuts import render, get_object_or_404

# Home Page
def home(request):
    return render(request, 'home.html')
