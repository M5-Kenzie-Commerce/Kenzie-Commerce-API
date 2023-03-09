from django.db import models
import uuid


class Address(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    state = models.CharField(max_length=2)
    city = models.CharField(max_length=60)
    district = models.CharField(max_length=60)
    street = models.CharField(max_length=130)
    zip_code = models.CharField(max_length=8)
    plus_information = models.TextField(null=True)
