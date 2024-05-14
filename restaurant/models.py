from django.db import models
# from users.models import UserModel
from django.utils import timezone

# Create your models here.
class CategoryModel(models.Model):
    class Meta:
        db_table = "categoryrestaurant"
        verbose_name_plural = "1. Category types"

    name = models.CharField(max_length=100, default="etc", verbose_name="Category name")
    
    def __str__(self):
        return str(self.name)

    
class RestaurantModel(models.Model):
    class Meta:
        db_table = "storerestaurant"
        verbose_name_plural = "2. Restaurant"

    name = models.CharField(
        max_length=100,
        verbose_name="Store name",
    )
    logo = models.FileField(
        null=True, blank=True, verbose_name="logo", upload_to="media/"
    )
    
    address = models.CharField(
        max_length=200,
        verbose_name="store location",
    )
    
    bannerimage = models.FileField(
        null=True, blank=True, verbose_name="bannerimage", upload_to="media/"
    )
    
    phone = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True, verbose_name="introduction")
    time = models.CharField(
        max_length=50,
        verbose_name="time",
    )

    def __str__(self):
        return str(self.name)

class FoodsModel(models.Model):
    class Meta:
        db_table = "goodsrestaurant"
        verbose_name_plural = "4. Food list"

    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="category",
    )
    
    image = models.FileField(
        null=True, blank=True, verbose_name="image", upload_to="media/"
    )
    name = models.CharField(max_length=100, verbose_name="product name")
    price = models.PositiveIntegerField(default=0, verbose_name="price")
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
    
class ImageModel(models.Model):
    class Meta:
        db_table = "imagerestaurant"
        verbose_name_plural = "5. Foods image list"

    foods = models.ForeignKey(
        FoodsModel, on_delete=models.CASCADE, verbose_name="Foods"
    )
    image = models.FileField(
        null=True, blank=True, verbose_name="image", upload_to="media/"
    )

    def __str__(self):
        return str(self.foods.name)

# New one
class Order(models.Model):
    STATUS_CHOICES = (
        ("Pending", "Pending"),
        ("Done", "Done"),
        ("Active", "Active"),
        ("Finish", "Finish"),
        ("Cancelled", "Cancelled"),
    )

    # user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    total_prices = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return f"Order {self.pk}, Status: {self.status}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(
        FoodsModel, on_delete=models.DO_NOTHING, related_name="orderitem"
    )
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"OrderItem {self.pk} - Product: {self.product.name}, Quantity: {self.quantity}"

