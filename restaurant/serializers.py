from rest_framework import serializers
from .models import (
    Category,
    Restaurant,
    Food,
    FoodImages,
    Order,
    OrderItem,
    Table
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        

