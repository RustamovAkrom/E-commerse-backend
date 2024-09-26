from django.shortcuts import render, get_object_or_404
from apps.cart.forms import CartAddProductForm
from .models import Category, Product


def home(request):
    products = Product.products.all()
    return render(request, "shop/index.html", {"products": products})


def product_list(request, category_slug=None):
    category = None
    categories = Category.categories.all()
    products = Product.products.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(
        request,
        "shop/shop.html",
        {"products": products, "categories": categories, "category": category},
    )


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    cart_product_form = CartAddProductForm()
    return render(
        request,
        "shop/single.html",
        {"product": product, "cart_product_form": cart_product_form},
    )


def about(request):
    return render(request, "shop/about.html")


def contact(request):
    return render(request, "shop/contact.html")
