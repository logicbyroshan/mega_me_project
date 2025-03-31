from django.shortcuts import render

# Home Page View
def home(request):
    return render(request, 'home.html')  # Renders the home page template
