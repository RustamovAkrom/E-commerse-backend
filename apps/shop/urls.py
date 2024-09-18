from django.urls import path
from . import views


app_name = 'shop'

urlpatterns = [
    path('', views.product_all, name='product_home'),
    path('<slug:slug>', views.product_detail, name='product_detail'),
    path('shop/<slug:category_slug>', views.category_link, name='category_list'),
]