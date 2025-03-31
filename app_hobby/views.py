from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Hobby, Product, Cart, Order

# Home Page
def home(request):
    return render(request, 'home.html')

# Hobby Section
def hobby(request):
    hobbies = Hobby.objects.all()
    return render(request, 'hobby.html', {'hobbies': hobbies})

def hobby_detail(request, hobby_id):
    hobby = get_object_or_404(Hobby, id=hobby_id)
    return render(request, 'hobby_detail.html', {'hobby': hobby})

@login_required
def hobby_new(request):
    if request.method == 'POST':
        Hobby.objects.create(name=request.POST.get('name'), user=request.user)
        return redirect('hobby')
    return render(request, 'hobby_new.html')

@login_required
def hobby_edit(request, hobby_id):
    hobby = get_object_or_404(Hobby, id=hobby_id, user=request.user)
    if request.method == 'POST':
        hobby.name = request.POST.get('name')
        hobby.save()
        return redirect('hobby_detail', hobby_id=hobby.id)
    return render(request, 'hobby_edit.html', {'hobby': hobby})

@login_required
def hobby_delete(request, hobby_id):
    hobby = get_object_or_404(Hobby, id=hobby_id, user=request.user)
    hobby.delete()
    return redirect('hobby')

# Product Section
def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})

# Cart Management
@login_required
def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    return render(request, 'cart.html', {'cart_items': cart_items})

@login_required
def cart_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Cart.objects.create(user=request.user, product=product)
    return JsonResponse({'message': f'{product.name} added to cart'})

@login_required
def cart_remove(request, product_id):
    cart_item = get_object_or_404(Cart, product_id=product_id, user=request.user)
    cart_item.delete()
    return JsonResponse({'message': 'Item removed from cart'})

@login_required
def cart_checkout(request):
    cart_items = Cart.objects.filter(user=request.user)
    if not cart_items:
        return JsonResponse({'error': 'Cart is empty'}, status=400)
    return render(request, 'cart_checkout.html', {'cart_items': cart_items})

def cart_checkout_success(request):
    return render(request, 'cart_checkout_success.html')

def cart_checkout_failure(request):
    return render(request, 'cart_checkout_failure.html')

def cart_checkout_cancel(request):
    return render(request, 'cart_checkout_cancel.html')

def cart_checkout_webhook(request):
    return JsonResponse({'message': 'Webhook received'}, status=200)

@login_required
def cart_checkout_confirm(request):
    return render(request, 'cart_checkout_confirm.html')

def cart_checkout_confirm_success(request):
    return render(request, 'cart_checkout_confirm_success.html')

def cart_checkout_confirm_failure(request):
    return render(request, 'cart_checkout_confirm_failure.html')

def cart_checkout_confirm_cancel(request):
    return render(request, 'cart_checkout_confirm_cancel.html')

def cart_checkout_confirm_webhook(request):
    return JsonResponse({'message': 'Confirm Webhook received'}, status=200)

# Order Management
@login_required
def orders(request):
    user_orders = Order.objects.filter(user=request.user)
    return render(request, 'orders.html', {'orders': user_orders})

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'order_detail.html', {'order': order})

@login_required
def order_new(request):
    if request.method == 'POST':
        Order.objects.create(user=request.user, total_price=request.POST.get('total_price'))
        return redirect('orders')
    return render(request, 'order_new.html')

@login_required
def order_edit(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if request.method == 'POST':
        order.total_price = request.POST.get('total_price')
        order.save()
        return redirect('order_detail', order_id=order.id)
    return render(request, 'order_edit.html', {'order': order})

# Product List View
def products_list(request):
    products = Product.objects.all()
    return render(request, 'products_list.html', {'products': products})
