from rest_framework import serializers
from .models import User
from addresses.models import Address
from addresses.serializers import AddressSerializer


class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "username",
            "is_superuser",
            "is_saller",
            "address",
            "password"
            ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user_address = validated_data.pop("address")
        address_obj = Address.objects.create(**user_address)

        if validated_data['is_superuser'] is True:
            return User.objects.create_superuser(**validated_data, address=address_obj)

        return User.objects.create_user(**validated_data, address=address_obj)

    def update(self, instance: User, validated_data: dict) -> User:
        new_address = validated_data.pop("address", None)
        new_password = validated_data.pop("password", None)

        if new_address:
            Address.objects.all().update(**new_address)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if new_password:
            instance.set_password(validated_data["password"])
        instance.save()

        return instance


class UserOrderSerializer(serializers.ModelSerializer):
    ...
