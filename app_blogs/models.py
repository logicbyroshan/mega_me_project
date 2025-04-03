from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.name

class Blog(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blogs')
    publish_date = models.DateTimeField(auto_now_add=True)
    read_time = models.IntegerField(help_text="Estimated read time in minutes")
    title = models.CharField(max_length=255)
    description = models.TextField()
    tags = models.CharField(max_length=500, help_text="Comma-separated tags")
    hero_image = models.ImageField(upload_to='blog_images/')
    content = HTMLField()
    likes = models.ManyToManyField(User, related_name='liked_blogs', blank=True)
    shares = models.ManyToManyField(User, related_name='shared_blogs', blank=True)
    
    def like_count(self):
        return self.likes.count()
    
    def share_count(self):
        return self.shares.count()
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Comment by {self.user.username} on {self.blog.title}'
class BlogUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.user.username

# Auto-generate username from email before saving
@receiver(pre_save, sender=User)
def auto_generate_username(sender, instance, **kwargs):
    if not instance.username:
        instance.username = instance.email.split('@')[0]  # Extract username from email