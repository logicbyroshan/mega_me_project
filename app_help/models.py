from django.db import models
from tinymce.models import HTMLField
from datetime import datetime
from datetime import date, time


# Session Model
class Content(models.Model):
    CATEGORY_CHOICES = [
        ("General", "General"),
        ("Education", "Education"),
        ("Technology", "Technology"),
        ("Other", "Other"),
    ]

    TAG_CHOICES = [
        ("Most Downloaded", "Most Downloaded"),
        ("Most Searched", "Most Searched"),
        ("Trending", "Trending"),
        ("New", "New"),
    ]

    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default="General")
    uploaded_at = models.DateTimeField(default=datetime.now)
    tag = models.CharField(max_length=100, choices=TAG_CHOICES, default="New")
    title = models.CharField(max_length=200, default="Untitled Content")
    description = models.TextField(default="No description provided.")
    file = models.FileField(upload_to='help/content_files/', null=True, blank=True)
    details = HTMLField(default="<p>More about this content...</p>")

    def __str__(self):
        return self.title

# Course Model
class Course(models.Model):
    title = models.CharField(max_length=200, default="Untitled Course")
    description = models.TextField(default="No course description provided.")
    price = models.CharField(max_length=100, default="Free")
    start_date = models.DateField(default=date.today)
    enrollment_count = models.PositiveIntegerField(default=0)
    duration = models.CharField(max_length=100, default="1 month")

    details = HTMLField(default="<p>Full course details go here...</p>")

    def __str__(self):
        return self.title

# Session Model    
class Session(models.Model):
    CATEGORY_CHOICES = [
        ("Career", "Career"),
        ("Tech", "Tech"),
        ("Education", "Education"),
        ("Other", "Other"),
    ]

    title = models.CharField(max_length=200, default="Untitled Session")
    description = models.TextField(default="No session description.")
    hero_image = models.ImageField(upload_to="help/session_hero/", null=True, blank=True)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default="Other")
    created_at = models.DateTimeField(auto_now_add=True)
    details = HTMLField(default="<p>More information about the session...</p>")

    available_date = models.DateField(default=date.today)
    available_time = models.TimeField(default=time(hour=10, minute=0))

    # Pricing tiers
    basic_price = models.CharField(max_length=100, default="₹199")
    basic_offerings = models.TextField(default="Basic Support, Q&A")

    premium_price = models.CharField(max_length=100, default="₹399")
    premium_offerings = models.TextField(default="Everything in Basic + Guidance + Notes")

    elite_price = models.CharField(max_length=100, default="₹699")
    elite_offerings = models.TextField(default="Everything in Premium + 1-on-1 Call + Project Review")

    def __str__(self):
        return self.title