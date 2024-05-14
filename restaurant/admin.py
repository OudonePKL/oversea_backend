from django.contrib import admin
from .models import Category, Restaurant, Food, FoodImages, Order, OrderItem, Table


admin.site.register(Category)
admin.site.register(Restaurant)
admin.site.register(Food)
admin.site.register(FoodImages)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Table)
