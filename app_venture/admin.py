from django.contrib import admin
from .models import (
    Startup, ProductImage, ProductDetail, ProductTimeline,
    TeamMember, USP, Milestone
)
from django import forms
from tinymce.widgets import TinyMCE


class StartupAdminForm(forms.ModelForm):
    overview = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 10}))
    bio = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 10}))
    problem = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 10}))
    solution = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 10}))

    class Meta:
        model = Startup
        fields = '__all__'


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductDetailInline(admin.StackedInline):
    model = ProductDetail
    extra = 1


class ProductTimelineInline(admin.StackedInline):
    model = ProductTimeline
    extra = 1


class TeamMemberInline(admin.StackedInline):
    model = TeamMember
    extra = 1


class USPInline(admin.StackedInline):
    model = USP
    extra = 1


class MilestoneInline(admin.StackedInline):
    model = Milestone
    extra = 1


@admin.register(Startup)
class StartupAdmin(admin.ModelAdmin):
    form = StartupAdminForm
    list_display = ('name', 'tagline')
    inlines = [
        ProductImageInline,
        ProductDetailInline,
        ProductTimelineInline,
        TeamMemberInline,
        USPInline,
        MilestoneInline
    ]
