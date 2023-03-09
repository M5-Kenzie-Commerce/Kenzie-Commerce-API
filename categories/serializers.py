from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "category_name"]

    def create(self, validated_data):
        ...

    def update(self, instance: Category, validated_data):
        ...
