from django.db import models
from tinymce.models import HTMLField


class Startup(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='startups/logos/')
    tagline = models.CharField(max_length=300)
    social_links = models.TextField(help_text="Add social links separated by commas (e.g., https://linkedin.com, https://twitter.com)")
    address = models.TextField()
    overview = HTMLField()
    bio = HTMLField()
    pitch_video = models.URLField(blank=True, null=True)
    pitch_file = models.FileField(upload_to='startups/pitches/', blank=True, null=True)
    problem = HTMLField()
    solution = HTMLField()

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    startup = models.ForeignKey(Startup, related_name='product_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='startups/products/')

    def __str__(self):
        return f"{self.startup.name} - Product Image"


class ProductDetail(models.Model):
    startup = models.ForeignKey(Startup, related_name='product_details', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    key_features = models.TextField(help_text="Add key features separated by commas")

    def get_feature_list(self):
        return [feature.strip() for feature in self.key_features.split(',') if feature.strip()]

    def __str__(self):
        return self.product_name


class ProductTimeline(models.Model):
    startup = models.ForeignKey(Startup, related_name='product_timelines', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.title} - {self.date}"


class TeamMember(models.Model):
    startup = models.ForeignKey(Startup, related_name='team_members', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    social_links = models.TextField(help_text="Comma-separated links")
    whatsapp = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.position}"


class USP(models.Model):
    startup = models.ForeignKey(Startup, related_name='usps', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='startups/usps/')
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class Milestone(models.Model):
    startup = models.ForeignKey(Startup, related_name='milestones', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='startups/milestones/')
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
