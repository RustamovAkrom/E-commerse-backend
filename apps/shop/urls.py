from django.urls import path
from . import views


app_name = 'shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_all, name='products'),
    path('product/<slug:slug>', views.product_detail, name='product_detail'),
    path('shop/<slug:category_slug>', views.category_link, name='category_list'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]