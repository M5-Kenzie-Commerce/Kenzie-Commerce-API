# Generated by Django 4.1.7 on 2023-03-10 07:28

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("categories", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="category",
            old_name="category_name",
            new_name="name",
        ),
    ]
