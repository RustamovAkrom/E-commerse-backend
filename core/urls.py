from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("account/", include("apps.account.urls", namespace="account")),
    path("cart/", include("apps.cart.urls", namespace="cart")),
    path("payment/", include("apps.payment.urls", namespace="payment")),
    path("coupons/", include("apps.coupons.urls", namespace="coupons")),
    path("orders/",include("apps.orders.urls", namespace="orders")),
    path("", include("apps.shop.urls", namespace="shop")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
