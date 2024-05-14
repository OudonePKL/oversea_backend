from django.urls import path
from restaurant import views

urlpatterns = [
    # Category
    path("category", views.CategoryListCreate.as_view(), name='category-list-create'),
    path("category/<int:pk>", views.CategoryDetail.as_view(), name='category-detail'),
    # Restaurant
    path("restaurant", views.RestaurantList.as_view(), name='restaurant-list'),
    path("restaurant/detail/<int:pk>", views.RestaurantRetrieve.as_view(), name='restaurant-detail'),
    # Food
    path("food", views.FoodList.as_view(), name='food-list'),
    path("food/create", views.FoodCreate.as_view(), name='food-create'),
    path("food/detail/<int:pk>", views.FoodRetrieve.as_view(), name='food-detail'),
    path("food/update/<int:pk>", views.FoodUpdate.as_view(), name='food-update'),
    path("food/delete/<int:pk>", views.FoodDestroy.as_view(), name='food-delete'),
    # Table
    path("table", views.TableList.as_view(), name='table-list'),
    path("table/create", views.TableCreate.as_view(), name='table-create'),
    path("table/detail/<int:pk>", views.TableRetrieve.as_view(), name='table-detail'),
    path("table/update/<int:pk>", views.TableUpdate.as_view(), name='table-update'),
    path("table/delete/<int:pk>", views.TableDestroy.as_view(), name='table-delete'),
]
