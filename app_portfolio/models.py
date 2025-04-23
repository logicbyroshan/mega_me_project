from django.db import models
from tinymce.models import HTMLField


class Skill(models.Model):
    PROGRESS_CHOICES = [
        ('beginner', 'Beginner'),
        ('expert', 'Expert'),
        ('done', 'Done'),
    ]

    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='skills/icons/', blank=True, null=True)
    progress_level = models.CharField(max_length=10, choices=PROGRESS_CHOICES, default='beginner')
    progress_percent = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    certificate = models.FileField(upload_to='skills/certificates/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.progress_level}"


class SkillResource(models.Model):
    RESOURCE_TYPES = [
        ('image', 'Image'),
        ('pdf', 'PDF'),
        ('video', 'Video'),
        ('link', 'External Link'),
    ]

    skill = models.ForeignKey(Skill, related_name='resources', on_delete=models.CASCADE)
    resource_type = models.CharField(max_length=10, choices=RESOURCE_TYPES)
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='skills/resources/files/', blank=True, null=True)
    image = models.ImageField(upload_to='skills/resources/images/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.skill.name} - {self.title} ({self.resource_type})"


class Experience(models.Model):
    STATUS_CHOICES = [
        ('joined', 'Just Joined'),
        ('working', 'Working'),
        ('left', 'Left'),
    ]

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='working')
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    position = models.CharField(max_length=100)
    company_name = models.CharField(max_length=150)
    company_logo = models.ImageField(upload_to='experience/company_logos/')
    short_description = models.TextField(blank=True)
    skills_used = models.ManyToManyField(Skill, related_name='experiences', blank=True)

    def __str__(self):
        return f"{self.position} at {self.company_name}"


class ExperienceImage(models.Model):
    experience = models.ForeignKey(Experience, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='experience/workplace_images/')

    def __str__(self):
        return f"Image for {self.experience}"


class Contribution(models.Model):
    experience = models.ForeignKey(Experience, related_name='contributions', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='experience/contributions/', blank=True, null=True)
    short_description = models.TextField(blank=True)
    detailed_description = HTMLField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.experience}"
    
class Project(models.Model):
    CATEGORY_CHOICES = [
        ('design', 'Design'),
        ('uiux', 'UI/UX'),
        ('development', 'Development'),
        ('other', 'Other'),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='development')
    title = models.CharField(max_length=200)
    short_description = models.TextField(blank=True)
    start_date = models.DateField()
    completion_date = models.DateField()
    tags = models.CharField(max_length=300, help_text='Comma-separated tags')

    def __str__(self):
        return self.title


class ProjectScreenshot(models.Model):
    project = models.ForeignKey(Project, related_name='screenshots', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects/screenshots/')

    def __str__(self):
        return f"Screenshot for {self.project.title}"


class ProjectSkill(models.Model):
    project = models.ForeignKey(Project, related_name='skills', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='projects/skills/icons/')

    def __str__(self):
        return f"{self.name} - {self.project.title}"


class ProjectFeature(models.Model):
    project = models.ForeignKey(Project, related_name='features', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    icon = models.ImageField(upload_to='projects/features/icons/')
    short_description = models.TextField(blank=True)
    detailed_description = HTMLField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.project.title}"


class Contributor(models.Model):
    project = models.ForeignKey(Project, related_name='contributors', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='projects/contributors/images/')
    social_links = models.JSONField(default=dict, help_text="Use JSON format: {'linkedin': 'url', 'github': 'url'}")

    def __str__(self):
        return f"{self.name} - {self.project.title}"