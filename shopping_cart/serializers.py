from rest_framework import serializers
from .models import CartProduct


class ShoppingCartSerializer(serializers.ModelSerializer):
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
