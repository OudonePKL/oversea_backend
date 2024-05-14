from django.db import models
from users.models import UserModel
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Category name")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

class Restaurant(models.Model):
    owner = models.ForeignKey(
        UserModel, on_delete=models.CASCADE, verbose_name="Owner"
    )
    name = models.CharField(
        max_length=100,
        verbose_name="Store name",
    )
    logo = models.FileField(
        null=True, blank=True, verbose_name="logo", upload_to="media/restaurant/"
    )

    address = models.CharField(
        max_length=200,
        verbose_name="Store location",
    )

    bannerimage = models.FileField(
        null=True, blank=True, verbose_name="Banner image", upload_to="media/restaurant/"
    )

    phone = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True, verbose_name="Introduction")
    time = models.CharField(
        max_length=50,
        verbose_name="Opening time",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

class Table(models.Model):
    name = models.CharField(max_length=10, verbose_name="Table number")
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, verbose_name="Restaurant"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

class Food(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name="Category",
    )
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, verbose_name="Restaurant"
    )
    image = models.FileField(
        null=True, blank=True, verbose_name="image", upload_to="media/restaurant/food/"
    )
    name = models.CharField(max_length=100, verbose_name="Product name")
    price = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

class FoodImages(models.Model):

    food = models.ForeignKey(Food, on_delete=models.CASCADE, verbose_name="Food")
    image = models.FileField(
        null=True, blank=True, verbose_name="Food image", upload_to="media/restaurant/food/"
    )

    def __str__(self):
        return str(self.foods.name)

class Order(models.Model):
    STATUS_CHOICES = (
        ("Pending", "Pending"),
        ("Done", "Done"),
        ("Active", "Active"),
        ("Finish", "Finish"),
        ("Cancelled", "Cancelled"),
    )

    table = models.ForeignKey(Table, on_delete=models.CASCADE, verbose_name="Table")
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, verbose_name="Restaurant"
    )
    total_prices = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.pk}, Status: {self.status}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Order id")
    food = models.ForeignKey(Food, on_delete=models.CASCADE, verbose_name="Food id")
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"OrderItem {self.pk} - Product: {self.product.name}, Quantity: {self.quantity}"
