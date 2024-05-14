from django.contrib import admin

from .models import (
    CategoryModel,
    RestaurantModel,
    FoodsModel,
    ImageModel,
    Order,
    OrderItem,
)


@admin.register(RestaurantModel)
class RestaurantAdmin(admin.ModelAdmin):
    """Board Admin Definition"""

    list_display = (
        "name",
        "logo",
        "address",
        "bannerimage",
        "phone",
        "description",
        "time",
    )

    search_fields = (
        "name",
    )


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    """Board Admin Definition"""

    list_display = ("id","name")

    search_fields = ("name",)


@admin.register(FoodsModel)
class FoodsAdmin(admin.ModelAdmin):
    """Board Admin Definition"""

    list_display = (
        "id",
        "category",
        "name",
        "price",
    )

    search_fields = ("name", "store")

    list_filter = ("category",)



@admin.register(ImageModel)
class ImageModelAdmin(admin.ModelAdmin):
    """Board Admin Definition"""

    list_display = ("id", "foods", "image")

    search_fields = ("foods",)
    
    

admin.site.register(Order)
admin.site.register(OrderItem)
