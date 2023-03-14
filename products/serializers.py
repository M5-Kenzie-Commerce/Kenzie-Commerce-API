from rest_framework import serializers
from .models import Product
from categories.serializers import CategorySerializer
from django.shortcuts import get_object_or_404
from users.models import User


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

    def stock_check(product):
        if product["stock"] == 0:
            return False
        return True

    def saller_check(user):
        return user.is_saller or user.is_superuser

    def create(self, validated_data: Product):
        product_user = get_object_or_404(
            User.objects.all(), email=validated_data["user"]
        )
        if not ProductSerializer.saller_check(product_user):
            raise serializers.ValidationError({"detail": "user not a saller"})
        category_obj = CategorySerializer.create_or_update_category(validated_data)
        validated_data["is_avaliable"] = ProductSerializer.stock_check(validated_data)
        return Product.objects.create(**validated_data, category=category_obj)

    def update(self, instance: Product, validated_data: dict) -> Product:
        if "user" in validated_data:
            raise serializers.ValidationError(
                {"detail": "product owner cannot be changed"}
            )
        if "name_product" in validated_data:
            raise serializers.ValidationError(
                {"detail": "product name cannot be changed"}
            )
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
