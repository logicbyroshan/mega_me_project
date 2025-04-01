from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from tinymce.models import HTMLField


# Skill Model

# Skill progress choices
SKILL_PROGRESS_CHOICES = [
    ("LEARNING", "Learning"),
    ("AVERAGE", "Average"),
    ("PROGRESS", "Progressing"),
    ("DONE", "Done"),
    ("EXPERT", "Expert"),
]

# Validation Function to Ensure Progress Constraints
def validate_progress(value, progress_level):
    limits = {
        "LEARNING": 10,
        "AVERAGE": 25,
        "PROGRESS": 50,
        "DONE": 75,
        "EXPERT": 100,
    }
    if value > limits.get(progress_level, 100):
        raise ValidationError(f"Progress cannot exceed {limits[progress_level]}% for '{progress_level}' level.")

class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    icon = models.ImageField(upload_to="skill_icons/", null=True, blank=True)
    progress_level = models.CharField(max_length=10, choices=SKILL_PROGRESS_CHOICES, default="LEARNING")
    progress = models.PositiveIntegerField(default=0)

    description = models.TextField(null=False, blank=False, default="No Description Provided")

    certificate = models.FileField(
        upload_to="skill_certificates/",
        null=True,
        blank=True,
        help_text="Upload PDF, DOCX, or an image as a certificate.",
    )

    def save(self, *args, **kwargs):
        """ Validate progress before saving """
        validate_progress(self.progress, self.progress_level)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.progress_level} ({self.progress}%)"

class SkillResource(models.Model):
    RESOURCE_TYPES = [
        ("IMAGE", "Image"),
        ("PDF", "PDF"),
        ("DOCX", "DOCX"),
        ("VIDEO", "YouTube Video"),
        ("LINK", "External Link"),
    ]

    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name="resources")
    resource_type = models.CharField(max_length=10, choices=RESOURCE_TYPES)
    file = models.FileField(upload_to="skill_resources/", null=True, blank=True)
    link = models.URLField(null=True, blank=True, help_text="For external links or YouTube videos.")

    def clean(self):
        """ Ensure at least a file or a link is provided """
        if not self.file and not self.link:
            raise ValidationError("Either a file or a link must be provided for a resource.")

    def __str__(self):
        return f"{self.skill.name} - {self.get_resource_type_display()}"



# Project Categories
PROJECT_CATEGORIES = [
    ("UI_UX", "UI-UX Project"),
    ("FRONTEND", "Frontend Project"),
    ("CLI", "Command Line Interface Project"),
    ("FULLSTACK", "Full Stack Project"),
    ("AI_ML", "AI-ML Project"),
    ("BACKEND", "Backend Project"),
    ("WEB_APP", "Web Application Project"),
    ("CROSS_PLATFORM", "Cross-Platform App"),
    ("NATIVE_APP", "Native App Project"),
    ("NLP", "NLP Project"),
    ("DEEP_LEARNING", "Deep Learning Project"),
    ("DATA_SCIENCE", "Data Science Project"),
    ("BIG_DATA", "Big Data Project"),
    ("CLOUD_APP", "Cloud Application Project"),
]


class Project(models.Model):
    category = models.CharField(max_length=20, choices=PROJECT_CATEGORIES, null=False, blank=False)
    completion_date = models.DateField(null=False, blank=False)
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    
    # Store tags as a comma-separated string
    tags = models.CharField(max_length=255, help_text="Enter tags separated by commas", null=False, blank=False)
    
    # Skills required for this project
    skills = models.ManyToManyField(Skill, blank=False)
    
    # TinyMCE for rich-text project details
    details = HTMLField(null=False, blank=False)

    def __str__(self):
        return self.title

    def get_tags_list(self):
        """Convert comma-separated tags into a Python list"""
        return self.tags.split(",") if self.tags else []

    def has_hero_image(self):
        """Ensure at least one image is set as hero"""
        return self.images.filter(is_hero=True).exists()

    def clean(self):
        """Validation to ensure at least one hero image exists"""
        if not self.has_hero_image():
            raise ValidationError("Each project must have at least one hero image.")

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="project_images/", null=False, blank=False)
    is_hero = models.BooleanField(default=False)  # One image should be set as the hero image

    def __str__(self):
        return f"{self.project.title} - Image"

class Feature(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="features")
    icon = models.CharField(max_length=255, null=False, blank=False, help_text="FontAwesome icon class (e.g., 'fas fa-robot')")
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=False, blank=False)

    def __str__(self):
        return f"{self.project.title} - {self.title}"


# Experience Model
class Experience(models.Model):
    position = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.position} at {self.company}"

# FAQ Model
class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question

class Subscription(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email