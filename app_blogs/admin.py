from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'publish_date', 'read_time', 'likes')
    search_fields = ('title', 'description', 'tags', 'category')
    list_filter = ('publish_date', 'category')
    prepopulated_fields = {'slug': ('title',)}
