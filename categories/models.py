from django.db import models
import uuid


class Category(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    category = models.CharField(max_length=100)
