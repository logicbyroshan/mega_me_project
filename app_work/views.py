from django.shortcuts import render, redirect

# Home Page
def home(request):
    return render(request, 'home.html')

