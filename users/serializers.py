from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "is_superuser", "is_saller", "adress_id"]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        if validated_data['is_superuser'] is True:
            return User.objects.create_superuser(**validated_data)
        return User.objects.create_user(**validated_data)


class UserOrderSerializer(serializers.ModelSerializer):
    ...
