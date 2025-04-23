from django.db import models
from tinymce.models import HTMLField
from django.utils.text import slugify
from django.contrib.auth.models import User
from datetime import datetime

class Blog(models.Model):
    title = models.CharField(max_length=200, default="Untitled Blog")
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(default="No description provided.")
    category = models.CharField(max_length=100, default="General")
    publish_date = models.DateField(default=datetime.now)
    read_time = models.PositiveIntegerField(default=3, help_text="Estimated read time in minutes")
    tags = models.CharField(max_length=300, default="blog", help_text="Comma-separated tags")
    hero_image = models.ImageField(upload_to='blogs/hero_images/', default='default_hero.jpg')
    content = HTMLField(default="<p>Start writing your blog here...</p>")
    likes = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.title

    def get_tags_list(self):
        return [tag.strip() for tag in self.tags.split(',') if tag.strip()]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("app_blogs:blog_detail", kwargs={"slug": self.slug})
