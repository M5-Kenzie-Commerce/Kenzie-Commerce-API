from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class OrderStatusChoices(models.TextChoices):
    order_placed = "Pedido Realizado"
    in_progress = "Em Andamento"
    delivered = "Entregue"


class User(AbstractUser):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(
        unique=True, error_messages={"error": "Email alredy exists"}
    )
    is_saller = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(null=True)
    is_superuser = models.BooleanField(default=False)

    address = models.OneToOneField(
        "addresses.Address",
        related_name="user",
        on_delete=models.CASCADE,
    )

    cart = models.OneToOneField(
        "shopping_cart.Cart",
        related_name="user",
        on_delete=models.CASCADE,
        null=True,
    )


class UserOrder(models.Model):
    ...


# Será necessário desenvolver uma model para armazenar
# os produtos que o usuário selecionou, antes de finalizar a compra.

# Associado a cada pedido deve conter seu status
# PEDIDO REALIZADO, EM ANDAMENTO ou ENTREGUE para acompanhamento do usuário.

# Deve conter todos os dados dos produtos, menos a quantidade em estoque..

# Deverá conter o horário que o pedido foi feito.
