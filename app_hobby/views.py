from django.views.generic import TemplateView, ListView
from .models import Book, Poem, Product

# Hobby Home Page
class HobbyHomeView(TemplateView):
    template_name = "hobby_app/hobby_home.html"

# Book List View
class BookListView(ListView):
    model = Book
    template_name = "hobby_app/hobby_book_list.html"
    context_object_name = "books"

# Poem List View
class PoemListView(ListView):
    model = Poem
    template_name = "hobby_app/hobby_poem_list.html"
    context_object_name = "poems"

# Product List View
class ProductListView(ListView):
    model = Product
    template_name = "hobby_app/hobby_product_list.html"
    context_object_name = "products"
