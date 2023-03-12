from rest_framework import serializers
from .models import Product
from categories.models import Category
from categories.serializers import CategorySerializer
from django.shortcuts import get_object_or_404
from users.models import User
from users.serializers import UserSerializer

# Deverá ter um estoque dos itens,
# quando o item estiver com 0 unidades deverá ter um campo
# indicando que o produto está indisponível.
# Somente um vendendor pode cadastrar/alterar produtos


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = [
            "id",
            "name_product",
            "price",
            "stock",
            "is_avaliable",
            "category",
            "user",
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "is_avaliable": {"read_only": True},
        }

    def stock_check(validated_data):
        if validated_data["stock"] == 0:
            return False
        return True

    def create(self, validated_data):
        category_obj = CategorySerializer.create_or_update_category(validated_data)
        get_object_or_404(User.objects.all(), email=validated_data["user"])
        validated_data["is_avaliable"] = ProductSerializer.stock_check(validated_data)
        return Product.objects.create(**validated_data, category=category_obj)

    def update(self, instance: Product, validated_data: dict) -> Product:
        get_object_or_404(User.objects.all(), email=validated_data["user"])
        if "category" in validated_data:
            category_obj = CategorySerializer.create_or_update_category(validated_data)
            instance.category = category_obj
        if "stock" in validated_data:
            instance.is_avaliable = ProductSerializer.stock_check(validated_data)
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()

        return instance


class ProductOrderSerializer(serializers.Serializer):
    ...
