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

    def create(self, validated_data):
        product_category = validated_data.pop("category")
        category_exist = Category.objects.filter(
            category__icontains=product_category["category"].lower()
        )
        category_obj = (
            category_exist.first()
            if category_exist.exists()
            else Category.objects.create(
                category=product_category["category"].lower()
            )
        )
        if validated_data["stock"] == 0:
            validated_data["is_avaliable"] = False

        return Product.objects.create(**validated_data, category=category_obj)

    def update(self, instance: Product, validated_data):
        ...

        return instance


class ProductOrderSerializer(serializers.Serializer):
    ...
