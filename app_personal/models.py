from django.db import models

class Education(models.Model):
    start_date = models.DateField()
    end_date = models.CharField(
        max_length=100,
        default="Currently Pursuing"
    )  # Using CharField to allow "Currently Pursuing"
    title = models.CharField(max_length=255, default="Degree/Program Title")
    institution = models.CharField(max_length=255, default="Institution Name")
    document = models.FileField(
        upload_to="personal/education/docs/",
        blank=True,
        null=True
    )  # For PDFs, Certificates, Results, etc.

    def __str__(self):
        return f"{self.title} at {self.institution}"


class Achievement(models.Model):
    image = models.ImageField(upload_to="personal/achievements/images/", default="default_achievement.jpg")
    title = models.CharField(max_length=255, default="Achievement Title")
    date = models.DateField()
    description = models.TextField(default="Description of the achievement.")
    document = models.FileField(upload_to="personal/achievements/docs/", blank=True, null=True)

    def __str__(self):
        return self.title
    

class Mention(models.Model):
    platform = models.CharField(max_length=100, default="Platform Name (e.g., Instagram, Twitter)")
    icon = models.ImageField(upload_to="personal/mentions/icons/", default="default_icon.png")  # platform icon or image
    date = models.DateField()
    handle = models.CharField(max_length=100, default="@username")
    message = models.CharField(max_length=255, default="Mention message or title")
    screenshot = models.ImageField(upload_to="personal/mentions/screenshots/", blank=True, null=True)
    link = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.platform} - {self.handle}"
    

class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    caption = models.CharField(max_length=255)
    tags = models.TextField(help_text="Enter comma-separated tags. Example: #sunset, #nature")

    def __str__(self):
        return self.caption

    def get_tag_list(self):
        return [tag.strip() for tag in self.tags.split(',') if tag.strip()]
    
class Problem(models.Model):
    LEVEL_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]

    PLATFORM_CHOICES = [
        ('codeforces', 'Codeforces'),
        ('leetcode', 'LeetCode'),
        ('gfg', 'GeeksForGeeks'),
        ('hackerrank', 'HackerRank'),
        ('codechef', 'CodeChef'),
        # Add more platforms as needed
    ]

    title = models.CharField(max_length=200)
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES)
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    problem_id = models.CharField(max_length=50, unique=True)
    code_block = models.TextField(help_text="Write your code here")

    def __str__(self):
        return f"{self.title} ({self.platform}, {self.level})"