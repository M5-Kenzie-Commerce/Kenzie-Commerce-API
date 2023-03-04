from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Address


class AdressSerializer(serializers.ModelSerializer):
    ...
