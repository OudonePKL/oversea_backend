from rest_framework import serializers
from .models import CategoryModel, RestaurantModel, FoodsModel, ImageModel, Order, OrderItem
# from users.serializers import UserSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantModel
        fields = '__all__'

class FoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodsModel
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = '__all__'


# Order
class OrderItemSerializer(serializers.ModelSerializer):
    product = FoodsSerializer()

    class Meta:
        model = OrderItem
        fields = ["id", "product", "quantity", "price", "color", "size"]


class OrderSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
    # user = UserSerializer()

    def get_items(self, obj):
        order_items = OrderItem.objects.filter(order=obj)
        serializer = OrderItemSerializer(order_items, many=True)
        return serializer.data

    class Meta:
        model = Order
        fields = [
            "id",
            "total_prices",
            "created_at",
            "status",
            "items",
        ]


class OrderItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ["id", "product", "quantity", "price"]


class OrderCreateSerializer(serializers.ModelSerializer):
    items = OrderItemCreateSerializer(many=True, write_only=True)

    def create(self, validated_data):
        order_items_data = validated_data.pop("items")
        order = Order.objects.create(**validated_data)
        for order_item_data in order_items_data:
            OrderItem.objects.create(order=order, **order_item_data)
        return order

    class Meta:
        model = Order
        fields = [
            "id",
            "total_prices",
            "created_at",
            "status",
            "items",
        ]


class OrderItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ["product", "quantity"]


class OrderUpdateSerializer(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        # Update order fields
        instance.status = validated_data.get("status", instance.status)
        instance.save()

        return instance

    class Meta:
        model = Order
        fields = ["status"]


class PendingOrderSerializer(OrderSerializer):
    class Meta:
        model = Order
        fields = [
            "id",
            "total_prices",
            "created_at",
            "status",
            "items",
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.status != "Pending":
            return None  # Skip orders that are not pending
        return data


class DoneOrderSerializer(OrderSerializer):
    class Meta:
        model = Order
        fields = [
            "id",
            "total_prices",
            "created_at",
            "status",
            "items",
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.status != "Done":
            return None  # Skip orders that are not Done
        return data

class ActiveOrderSerializer(OrderSerializer):
    class Meta:
        model = Order
        fields = [
            "id",
            "total_prices",
            "created_at",
            "status",
            "items",
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.status != "Active":
            return None  # Skip orders that are not Active
        return data

class FinishOrderSerializer(OrderSerializer):
    class Meta:
        model = Order
        fields = [
            "id",

            "total_prices",
            "created_at",
            "status",
            "items",
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.status != "Finish":
            return None  # Skip orders that are not Finish
        return data
