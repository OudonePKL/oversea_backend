from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant2 import views

router = DefaultRouter()
router.register(r'tables', views.TableViewSet, basename='table')
router.register(r'menu-items', views.MenuItemViewSet, basename='menuitem')
router.register(r'orders', views.OrderViewSet, basename="orders")
router.register(r'order-items', views.OrderItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # Category
    path("category", views.CategoryListCreate.as_view(), name="category-list-create"),
    path("category/<int:pk>", views.CategoryDetail.as_view(), name="category-detail"),
    # Restaurant
    path("restaurant", views.RestaurantList.as_view(), name="restaurant-list"),
    path(
        "restaurant/detail/<int:pk>",
        views.RestaurantRetrieve.as_view(),
        name="restaurant-detail",
    ),
]
