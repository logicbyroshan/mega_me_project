from django.contrib import admin
from .models import Content, Course, Session

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'tag', 'uploaded_at')
    search_fields = ('title', 'description', 'tag')
    list_filter = ('category', 'tag', 'uploaded_at')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'start_date', 'enrollment_count')
    search_fields = ('title', 'description')
    list_filter = ('start_date', 'price')


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'available_date', 'available_time', 'created_at')
    list_filter = ('category', 'available_date')
    search_fields = ('title', 'description')