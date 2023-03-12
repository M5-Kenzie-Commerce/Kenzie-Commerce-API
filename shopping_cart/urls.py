from django.urls import path
from . import views

urlpatterns = [
    path("shopping_cart/<str:product_id>/", views.ShoppingCart.as_view()),
    path(
        "shopping_cart_up/<str:shopping_cart_id>/",
        views.ShoppingCartUpdateView.as_view(),
    ),
    path("cart/<str:cart_id>/", views.CartDetailView.as_view()),
]
