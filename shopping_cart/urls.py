from django.urls import path
from . import views

urlpatterns = [
    path("shopping_cart/<str:product_id>/", views.ShoppingCart.as_view()),
    path("cart/<str:cart_id>/", views.CartDetailView.as_view()),
]
