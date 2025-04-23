from django.contrib import admin
from .models import Service, PricingPackage, PackageFeature
from django import forms
from tinymce.widgets import TinyMCE


class ServiceAdminForm(forms.ModelForm):
    detailed_description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 20}))
    class Meta:
        model = Service
        fields = '__all__'


class PackageFeatureInline(admin.TabularInline):
    model = PackageFeature
    extra = 1


class PricingPackageInline(admin.StackedInline):
    model = PricingPackage
    extra = 1
    inlines = [PackageFeatureInline]

class PricingPackageAdmin(admin.ModelAdmin):
    inlines = [PackageFeatureInline]
    list_display = ('service', 'package_type', 'price')
    list_filter = ('package_type',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    form = ServiceAdminForm
    list_display = ('title', 'category')
    inlines = [PricingPackageInline]
    search_fields = ('title', 'category')
    list_filter = ('category',)


admin.site.register(PricingPackage, PricingPackageAdmin)
