from django.contrib import admin
from .models import Category, Restaurant, Table, MenuItem, Order, OrderItem


admin.site.register(Category)
admin.site.register(Restaurant)
admin.site.register(Table)
admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(OrderItem)