from django.db import models
from tinymce.models import HTMLField

class Product(models.Model):
    title = models.CharField(max_length=255, default="Untitled Product")
    short_description = models.TextField(default="Short description of the product.")
    mrp = models.DecimalField(max_digits=10, decimal_places=2, default=999.99)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, default=499.99)
    detailed_description = HTMLField(default="<p>More details about the product...</p>")

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="hobby/products/")

    def __str__(self):
        return f"Image for {self.product.title}"


class Poem(models.Model):
    image = models.ImageField(upload_to="hobby/poems/", default="default_poem.jpg")
    poet_name = models.CharField(max_length=100, default="Anonymous")
    date_published = models.DateField(auto_now_add=True)
    content = models.TextField(default="This is a beautiful poem...")

    def __str__(self):
        return f"{self.poet_name}'s Poem ({self.date_published})"
    

class Book(models.Model):
    image = models.ImageField(upload_to="hobby/books/", default="default_book.jpg")
    title = models.CharField(max_length=255, default="Untitled Book")
    author = models.CharField(max_length=100, default="Unknown Author")
    mrp = models.DecimalField(max_digits=10, decimal_places=2, default=499.99)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=299.99)
    description = HTMLField(default="<p>About the book...</p>")
    file = models.FileField(upload_to="hobby/books/files/", blank=True, null=True)

    def __str__(self):
        return self.title