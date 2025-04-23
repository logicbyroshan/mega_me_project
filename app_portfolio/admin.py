from django.contrib import admin
from .models import Skill, SkillResource, Experience, ExperienceImage, Contribution, SkillResource, ProjectScreenshot, ProjectSkill, ProjectFeature, Project, Contributor


class SkillResourceInline(admin.StackedInline):
    model = SkillResource
    extra = 1


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'progress_level', 'progress_percent')
    inlines = [SkillResourceInline]
    search_fields = ('name', 'description')
    list_filter = ('progress_level',)



class ExperienceImageInline(admin.TabularInline):
    model = ExperienceImage
    extra = 1


class ContributionInline(admin.StackedInline):
    model = Contribution
    extra = 1


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'company_name', 'status', 'start_date', 'end_date')
    search_fields = ('position', 'company_name')
    list_filter = ('status',)
    inlines = [ExperienceImageInline, ContributionInline]


class ProjectScreenshotInline(admin.TabularInline):
    model = ProjectScreenshot
    extra = 1


class ProjectSkillInline(admin.TabularInline):
    model = ProjectSkill
    extra = 1


class ProjectFeatureInline(admin.StackedInline):
    model = ProjectFeature
    extra = 1


class ContributorInline(admin.StackedInline):
    model = Contributor
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'start_date', 'completion_date')
    search_fields = ('title', 'tags')
    list_filter = ('category',)
    inlines = [ProjectScreenshotInline, ProjectSkillInline, ProjectFeatureInline, ContributorInline]