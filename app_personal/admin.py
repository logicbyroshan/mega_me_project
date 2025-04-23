from django.contrib import admin
from django import forms
from tinymce.widgets import TinyMCE
from .models import Education, Achievement, Mention, Photo, Problem

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('title', 'institution', 'start_date', 'end_date')

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')

@admin.register(Mention)
class MentionAdmin(admin.ModelAdmin):
    list_display = ('platform', 'handle', 'date')

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'caption', 'image_preview', 'formatted_tags')
    search_fields = ('caption', 'tags')
    readonly_fields = ('image_preview',)

    def formatted_tags(self, obj):
        return ", ".join(obj.get_tag_list())
    formatted_tags.short_description = 'Tags'

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="height: 100px;" />'
        return "(No image)"
    image_preview.allow_tags = True
    image_preview.short_description = 'Image Preview'


class ProblemAdminForm(forms.ModelForm):
    code_block = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 20}))

    class Meta:
        model = Problem
        fields = '__all__'

@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    form = ProblemAdminForm
    list_display = ('title', 'platform', 'level', 'problem_id')
    search_fields = ('title', 'problem_id')
    list_filter = ('platform', 'level')