DJANGO_DEFAULT_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

PROJECT_APPS = [
    "apps.shared.apps.SharedConfig",
    "apps.shop.apps.ShopConfig",
    "apps.orders.apps.OrdersConfig",
    "apps.account.apps.AccountConfig",
    "apps.cart.apps.CartConfig",
    "apps.checkout.apps.CheckoutConfig",
    "apps.coupons.apps.CouponsConfig",
]

THIRTY_PARTY_APPS = [
    "modeltranslation",
]
