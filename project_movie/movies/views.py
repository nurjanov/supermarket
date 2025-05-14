from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .cart import SessionCart

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def add_to_cart(request, product_id):
    cart = SessionCart(request)
    cart.add(product_id)
    return redirect('product_list')

def view_cart(request):
    cart = SessionCart(request)
    products = Product.objects.filter(id__in=cart.items().keys())
    cart_items = [(product, cart.items().get(str(product.id))) for product in products]
    return render(request, 'cart.html', {'cart_items': cart_items})