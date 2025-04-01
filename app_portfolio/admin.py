from django.contrib import admin
from .models import Skill, SkillResource, Project, ProjectImage, Feature


class SkillResourceInline(admin.TabularInline):
    model = SkillResource
    extra = 1  # Allow adding new resources from Skill admin

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    inlines = [SkillResourceInline]  # Manage resources inside Skill
    list_display = ("name", "progress_level", "progress")


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1  # Allow adding new images from Project admin
    min_num = 1  # At least 1 image required

class FeatureInline(admin.TabularInline):
    model = Feature
    extra = 1  # Allow adding new features from Project admin
    min_num = 1  # At least 1 feature required

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline, FeatureInline]  # Manage images & features inside Project
    list_display = ("title", "category", "completion_date")

