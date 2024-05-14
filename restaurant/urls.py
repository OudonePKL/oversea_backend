from django.urls import path
from . import views
urlpatterns = [
    path("category", views.CategoryListCreate.as_view(), name='category-list-create'),
    path("category/<int:pk>", views.CategoryDetail.as_view(), name='category-detail-update-delete'),
   
]
