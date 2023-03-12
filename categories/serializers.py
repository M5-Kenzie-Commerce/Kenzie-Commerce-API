from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "category"]

    def create(validated_data):
        ...

    def update(self, instance: Category, validated_data):
        ...

    def create_or_update_category(validated_data):
        product_category = validated_data.pop("category")
        category_exist = Category.objects.filter(
            category__icontains=product_category["category"].lower()
        )
        category_obj = (
            category_exist.first()
            if category_exist.exists()
            else Category.objects.create(category=product_category["category"].lower())
        )
        return category_obj
