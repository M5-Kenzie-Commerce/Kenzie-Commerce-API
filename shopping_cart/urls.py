from django.urls import path
from . import views

urlpatterns = [
    path("shopping_cart/", views.ShoppingCart.as_view()),
]