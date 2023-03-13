from django.db import models
import uuid


class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    products = models.ManyToManyField(
        "products.Product",
        through="shopping_cart.CartProduct",
        related_name="carts",
    )


class CartProduct(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    cart = models.ForeignKey(
        "shopping_cart.Cart",
        on_delete=models.CASCADE,
        related_name="cart_cart_products",
    )

    product = models.ForeignKey(
        "products.Product",
        on_delete=models.CASCADE,
        related_name="product_cart_products",
    )

    amount = models.PositiveIntegerField()
    createdAt = models.DateTimeField(auto_now_add=True)
