from django.contrib import admin
from .models import Product, ProductImage, Poem, Book

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'mrp', 'selling_price')
    inlines = [ProductImageInline]


@admin.register(Poem)
class PoemAdmin(admin.ModelAdmin):
    list_display = ('poet_name', 'date_published')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'mrp', 'price')