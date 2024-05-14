from rest_framework import serializers
from .models import Category, Restaurant, Food, FoodImages, Table, Order, OrderItem
from users.serializers import UserSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class OnlyRestaurantInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"


class RestaurantSerializer(serializers.ModelSerializer):
    restaurant = UserSerializer()
    menu_set = serializers.SerializerMethodField()
    table_set = serializers.SerializerMethodField()

    def get_menu_set(self, obj):
        foods = Food.objects.filter(restaurant_id=obj.id)
        serializer = OnlyStoreFoodSerializer(foods, many=True)
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


# class FoodSerializer(serializers.ModelSerializer):
#     restaurant = RestaurantSerializer()
#     category = CategorySerializer()

#     class Meta:
#         model = Food
#         fields = "__all__"

# fields = ["name", "price", "description", "created_at", "updated_at", "image", "category", "restaurant"]


class OnlyStoreFoodSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    image_set = serializers.SerializerMethodField()

    def get_category(self, obj):
        return obj.category.name

    def get_image_set(self, obj):
        images = FoodImages.objects.filter(food_id=obj.id)
        serializer = FoodImagesSerializer(images, many=True)
        image_set = [i["image"] for i in serializer.data]
        return image_set

    class Meta:
        model = Food
        exclude = ["created_at", "updated_at", "restaurant"]


class FoodSerializer(serializers.ModelSerializer):
    restaurant_name = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    image_set = serializers.SerializerMethodField()

    def get_restaurant_name(self, obj):
        restaurant_name = obj.restaurant.name
        if len(restaurant_name) >= 15:
            restaurant_name = f"{restaurant_name[:15]}..."
        return restaurant_name

    def get_category(self, obj):
        return obj.category.name

    def get_image_set(self, obj):
        images = FoodImages.objects.filter(food_id=obj.id)
        serializer = FoodImagesSerializer(images, many=True)
        image_set = [i["image"] for i in serializer.data]
        return image_set

    class Meta:
        model = Food
        fields = "__all__"


class FoodManageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = "__all__"


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = "__all__"


class TableManageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = "__all__"


class FoodImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodImages
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderManageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"
