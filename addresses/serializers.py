from rest_framework import serializers
from .models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            "id",
            "state",
            "city",
            "district",
            "street",
            "zip_code",
            "plus_information"
            ]

    def create(self, validated_data):
        return Address.objects.create(**validated_data)
