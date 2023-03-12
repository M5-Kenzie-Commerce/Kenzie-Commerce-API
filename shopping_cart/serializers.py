from rest_framework import serializers
from .models import CartProduct, Cart
from products.serializers import ProductSerializer


class ShoppingCartSerializer(serializers.ModelSerializer):
    def update(self, instance: CartProduct, validated_data: dict):
        if validated_data["amount"] == 0:
            instance.delete()

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance

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
