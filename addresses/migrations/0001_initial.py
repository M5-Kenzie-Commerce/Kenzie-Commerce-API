# Generated by Django 4.1.7 on 2023-03-12 23:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("state", models.CharField(max_length=2)),
                ("city", models.CharField(max_length=60)),
                ("district", models.CharField(max_length=60)),
                ("street", models.CharField(max_length=130)),
                ("zip_code", models.CharField(max_length=8)),
                ("plus_information", models.TextField(null=True)),
            ],
        ),
    ]
