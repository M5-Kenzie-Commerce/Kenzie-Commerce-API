from rest_framework import serializers
from .models import CartProduct, Cart
from products.serializers import ProductSerializer


class ShoppingCartSerializer(serializers.ModelSerializer):
    product = ProductSerializer

    class Meta:
        model = CartProduct
        fields = [
            "id",
            "cart",
            "product",
            "amount",
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "cart": {"read_only": True},
            "product": {"read_only": True},
        }


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = [
            "id",
            "cart_cart_products",
            "products",
        ]

        depth = 1
