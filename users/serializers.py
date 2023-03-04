from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    ...


class UserOrderSerializer(serializers.ModelSerializer):
    ...
