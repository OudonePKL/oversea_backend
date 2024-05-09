from django.contrib import admin

from .models import (
    CategoryModel,
    StoreModel,
    GoodsModel,
    ImageModel,
    Order,
    OrderItem,
)


@admin.register(StoreModel)
class StoreAdmin(admin.ModelAdmin):
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


@admin.register(GoodsModel)
class GoodsAdmin(admin.ModelAdmin):
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

    list_display = ("id", "goods", "image")

    search_fields = ("goods",)
    
    

admin.site.register(Order)
admin.site.register(OrderItem)
