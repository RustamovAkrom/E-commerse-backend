from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def product_all(request):
    products = Product.products.all()
    return render(request, 'shop/index.html', {'products': products})


def category_link(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.products.filter(category=category)
    return render(request, 'shop/category.html', {'category': category, 'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'shop/single.html', {'product': product})
