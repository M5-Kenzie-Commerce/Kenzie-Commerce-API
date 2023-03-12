from django.db import models
import uuid


class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name_product = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.PositiveIntegerField(default=1)
    is_avaliable = models.BooleanField(default=True)

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="products"
    )

    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.CASCADE,
        related_name="products",
    )

    def __repr__(self) -> str:
        return f"<[{self.id}] {self.name_product} - {self.user}>"
