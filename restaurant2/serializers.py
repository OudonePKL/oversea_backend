from rest_framework import serializers
from .models import Category, Restaurant, Table, MenuItem, Order, OrderItem
from users.serializers import UserSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class RestaurantSerializer(serializers.ModelSerializer):
    restaurant = UserSerializer()
    menu_set = serializers.SerializerMethodField()
    table_set = serializers.SerializerMethodField()

    def get_menu_set(self, obj):
        menu_item = MenuItem.objects.filter(restaurant_id=obj.id)
        serializer = MenuItemSerializer(menu_item, many=True)
        return serializer.data

    def get_table_set(self, obj):
        tables = Table.objects.filter(restaurant_id=obj.id)
        serializer = TableSerializer(tables, many=True)
        return serializer.data

    class Meta:
        model = Restaurant
        fields = "__all__"


class RestaurantManageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = "__all__"


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ["menu_item", "quantity"]


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ["id", "restaurant", "table", "status", "paid", "order_items"]

    def create(self, validated_data):
        items_data = validated_data.pop("order_items")
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order

    def update(self, instance, validated_data):
        items_data = validated_data.pop("order_items", None)

        instance.table = validated_data.get("table", instance.table)
        instance.status = validated_data.get("status", instance.status)
        instance.paid = validated_data.get("paid", instance.paid)
        instance.save()

        if items_data:
            # Clear existing order order_items and create new ones
            instance.order_items.all().delete()
            for item_data in items_data:
                OrderItem.objects.create(order=instance, **item_data)

        return instance
