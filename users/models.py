from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class OrderStatusChoices(models.TextChoices):
    order_placed = "Pedido Realizado"
    in_progress = "Em Andamento"
    delivered = "Entregue"


class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(unique=True, error_messages={"error": "Email alredy exists"})
    is_saller = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(null=True)
    is_superuser = models.BooleanField(default=False)

    address = models.OneToOneField("addresses.Address", related_name="user", on_delete=models.CASCADE)


class UserOrder(models.Model):
    order_status: models.CharField(
        max_length=30, choices=OrderStatusChoices, default=OrderStatusChoices.order_placed
    )
    ordered_at = models.DateTimeField(auto_now_add=True)
    ordered_by = models.ForeignKey(
        "users.User", on_delete=models.PROTECT, related_name="orders"
    )
    product = models.ForeignKey(
        "shopping_cart", on_delete=models.PROTECT, related_name="orders"
    )