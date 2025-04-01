from django.contrib import admin
from .models import Skill, SkillResource, Project, ProjectImage, Feature, Experience, ExperienceImage, PersonalInfo


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

class ExperienceImageInline(admin.TabularInline):
    model = ExperienceImage
    extra = 1  # Number of empty forms to display

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'status', 'start_date', 'end_date')
    search_fields = ('position', 'description')
    list_filter = ('status', 'start_date', 'end_date')
    filter_horizontal = ('skills',)
    inlines = [ExperienceImageInline]
    fieldsets = (
        ('Basic Information', {
            'fields': ('position', 'status', 'start_date', 'end_date')
        }),
        ('Details', {
            'fields': ('description', 'skills', 'contributions', 'detailed_blog')
        }),
    )

@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'total_projects', 'years_of_experience')
    search_fields = ('name',)
    list_filter = ('years_of_experience',)
    fieldsets = (
        ('Basic Information', {'fields': ('name', 'profile_image')}),
        ('Career Stats', {'fields': ('total_projects', 'years_of_experience')}),
        ('About', {'fields': ('about_me', 'titles', 'detailed_description')}),
    )