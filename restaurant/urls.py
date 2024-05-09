from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryListCreate.as_view(), name='category-list'),
    path('stores/', views.StoreListCreate.as_view(), name='store-list'),
    path('goods/', views.GoodsListCreate.as_view(), name='goods-list'),
    path('images/', views.ImageListCreate.as_view(), name='image-list'),
    
    # new order
    path('orders', views.OrderListView.as_view(), name='order-list'),
    path('order/create', views.OrderCreateAPIView.as_view(), name='order-create'),
    path('order/update/<int:pk>', views.OrderUpdateAPIView.as_view(), name='order-update'),
    path('order/<int:pk>', views.OrderDetailView.as_view(), name='order-detail'),
    path('user/<int:user_id>/order', views.UserOrderListView.as_view(), name='user-order-list'),
    path('order/delete/<int:pk>', views.OrderDeleteView.as_view(), name='delete-order'),
    path('order/pending/', views.PendingOrderListAPIView.as_view(), name='pending-orders'),
    path('order/done/', views.DoneOrderListAPIView.as_view(), name='done-orders'),
    path('order/active/', views.ActiveOrderListAPIView.as_view(), name='active-orders'),
    path('order/finish/', views.FinishOrderListAPIView.as_view(), name='finish-orders'),
]
