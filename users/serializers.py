from rest_framework import serializers
from .models import User, UserOrder
import users.views as classes
from addresses.models import Address
from shopping_cart.models import Cart
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
            "createdAt",
            "updatedAt",
            "address",
            "cart_id",
            "password",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "cart_id": {"read_only": True},
            "createdAt": {"read_only": True},
            "updatedAt": {"read_only": True},
        }

    def create(self, validated_data):
        user_address = validated_data.pop("address")
        address_obj = Address.objects.create(**user_address)

        cart = Cart.objects.create()

        if validated_data["is_superuser"] is True:
            return User.objects.create_superuser(
                **validated_data,
                address=address_obj,
                cart=cart,
            )

        return User.objects.create_user(
            **validated_data,
            address=address_obj,
            cart=cart,
        )

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

    ordered_by = UserSerializer(read_only=True)

    def update(self, instance: UserOrder, validated_data: dict) -> UserOrder:

        instance.order_status = validated_data["order_status"]

        instance.save()

        classes.Email.email_message(
            self,
            user_email=instance.ordered_by.email,
            message=f"""
            <body style="border: 1px solid black; width: 70%; margin: 0px auto">
                <header style="background-color: black; color: white; padding: 10px 0px 10px 15px; ">
                    <h1 style="font-family: Arial, Helvetica, sans-serif;">Atualização do Pedido</h1>
                </header>
                <main style="background-color: whitesmoke;">
                    <p style="font-size: 1rem; margin-left: 10px; font-weight: 500">Olá, {instance.ordered_by.first_name}</p>
                    <p style="font-size: 1rem; margin-left: 10px; font-weight: 500">O seu pedido do produto <b>{instance.product.name_product}</b> teve o estatus atualizado para <b>{instance.order_status}</b></p>
                    <p style="font-size: 1rem; margin-left: 10px; font-weight: 500">Obrigado por comprar conosco!</p>
                </main>
            </body>
            """,
        )

        return instance

    class Meta:

        model = UserOrder
        fields = ["id", "order_status", "ordered_at", "product", "ordered_by", "amount"]
        read_only_fields = [
            "id",
            "ordered_at",
            "product",
            "ordered_by",
            "amount"
        ]
        depth = 0
