# Generated by Django 4.2.4 on 2024-03-11 09:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="goodsmodel",
            name="is_popular",
        ),
        migrations.AddField(
            model_name="categorymodel",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="media/"),
        ),
        migrations.AddField(
            model_name="goodsmodel",
            name="description",
            field=models.TextField(blank=True),
        ),
    ]
