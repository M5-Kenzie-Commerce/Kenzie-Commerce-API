from django.db import models
import uuid


class CartProduct(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    cart = models.ForeignKey(
        "users.Cart", on_delete=models.CASCADE, related_name="cart_products"
    )

    product = models.ForeignKey(
        "products.Product",
        on_delete=models.CASCADE,
        related_name="product_cart_products",
    )

    amount = models.PositiveIntegerField()


# Fazer o relacionamento many-to-many(Product => Cart) indicando a tabela pivo CartProduct
