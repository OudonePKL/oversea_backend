# Generated by Django 4.2.4 on 2024-05-14 03:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="usermodel",
            name="is_restaurant",
            field=models.BooleanField(default=False, verbose_name="Restaurant"),
        ),
    ]
