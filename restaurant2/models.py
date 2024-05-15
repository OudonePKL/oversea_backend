from django.db import models
from users.models import UserModel
from django.utils import timezone
import qrcode
from io import BytesIO
from django.core.files import File


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
        null=True, blank=True, verbose_name="bannerimage", upload_to="media/restaurant/"
    )

    phone = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True, verbose_name="introduction")
    time = models.CharField(
        max_length=50,
        verbose_name="Opening time",
    )

    def __str__(self):
        return str(self.name)


class Table(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, verbose_name="Restaurant"
    )
    number = models.PositiveIntegerField()
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True)

    def save(self, *args, **kwargs):
        # Generate the QR code
        qr_url = f"http://localhost/table/{self.number}/order"
        qr = qrcode.make(qr_url)
        qr_io = BytesIO()
        qr.save(qr_io, 'PNG')
        qr_file = File(qr_io, name=f"{self.number}.png")
        self.qr_code.save(f"{self.number}.png", qr_file, save=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Restaurant: {self.restaurant.name} - Table: {self.number}"

    def is_available(self):
        # A table is considered available if there are no pending or preparing orders associated with it
        return not self.order_set.filter(status__in=['PENDING', 'PREPARING']).exists()


class MenuItem(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, verbose_name="Restaurant"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name="category",
    )
    
    image = models.FileField(
        null=True, blank=True, verbose_name="image", upload_to="media/restaurant/MenuItem"
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Restaurant: {self.restaurant.name} - Munu item: {self.name}"



class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PREPARING', 'Preparing'),
        ('READY', 'Ready'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.PROTECT, verbose_name="Restaurant"
    )
    table = models.ForeignKey(Table, on_delete=models.PROTECT)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.id} at Table {self.table.number}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name} for Order {self.order.id}"


