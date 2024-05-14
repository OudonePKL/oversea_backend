from django.db import models
from users.models import UserModel
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100, default="etc", verbose_name="Category name")
    
    def __str__(self):
        return str(self.name)

    
class Restaurant(models.Model):
    restaurant = models.ForeignKey(
        UserModel, on_delete=models.CASCADE, verbose_name="Restaurant owner"
    )
    name = models.CharField(
        max_length=100,
        verbose_name="restaurant name",
    )
    logo = models.FileField(
        null=True, blank=True, verbose_name="logo", upload_to="media/restaurant/"
    )
    
    address = models.CharField(
        max_length=200,
        verbose_name="restaurant location",
    )
    
    bannerimage = models.FileField(
        null=True, blank=True, verbose_name="bannerimage", upload_to="media/"
    )
    
    phone = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True, verbose_name="introduction")
    time = models.CharField(
        max_length=50,
        verbose_name="Opening time",
    )

    def __str__(self):
        return str(self.name)

class Food(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, verbose_name="Restaurant"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name="category",
    )
    
    image = models.FileField(
        null=True, blank=True, verbose_name="image", upload_to="media/restaurant/Food"
    )
    name = models.CharField(max_length=100, verbose_name="menu")
    price = models.PositiveIntegerField(default=0, verbose_name="price")
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
    
class Table(models.Model):
    name = models.CharField(max_length=20, verbose_name="Table number")
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, verbose_name="Restaurant"
    )
    is_available = models.BooleanField(default=True)
    qrcode = models.CharField(max_length=255, default="http://127.0.0.1:8000/admin/restaurant/table/add/$table=003")
    
class FoodImages(models.Model):
    food = models.ForeignKey(
        Food, on_delete=models.CASCADE, verbose_name="Food"
    )
    image = models.FileField(
        null=True, blank=True, verbose_name="image", upload_to="media/restaurant/Food"
    )

    def __str__(self):
        return str(self.food.name)

class Order(models.Model):
    STATUS_CHOICES = (
        ("Pending", "Pending"),
        ("Processing", "Processing"),
        ("Shipped", "Shipped"),
        ("Delivered", "Delivered"),
        ("Cancelled", "Cancelled"),
    )
    table = models.ForeignKey(Table, on_delete=models.PROTECT)
    total_prices = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return f"Order {self.pk}, Status: {self.status}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    food = models.ForeignKey(
        Food, on_delete=models.PROTECT, related_name="orderitem"
    )
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"OrderItem {self.pk} - Product: {self.product.name}, Quantity: {self.quantity}"

