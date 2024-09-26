from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("account/", include("apps.account.urls")),
    # path("cart/", include("apps.cart.urls")),
    # path("checkout/", include("apps.checkout.urls")),
    # path("orders/",include("apps.orders.urls")),
    path("", include("apps.shop.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
