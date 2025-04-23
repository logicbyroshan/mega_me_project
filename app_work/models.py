from django.db import models
from tinymce.models import HTMLField


class Service(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=300)
    hero_image = models.ImageField(upload_to='services/')
    detailed_description = HTMLField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class PricingPackage(models.Model):
    PACKAGE_CHOICES = [
        ('basic', 'Basic'),
        ('standard', 'Standard'),
        ('premium', 'Premium'),
    ]

    service = models.ForeignKey(Service, related_name='packages', on_delete=models.CASCADE)
    package_type = models.CharField(max_length=10, choices=PACKAGE_CHOICES)
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    short_detail = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.service.title} - {self.package_type}"


class PackageFeature(models.Model):
    pricing_package = models.ForeignKey(PricingPackage, related_name='features', on_delete=models.CASCADE)
    feature = models.CharField(max_length=200)
    extra_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.feature} ({self.pricing_package.package_type})"
