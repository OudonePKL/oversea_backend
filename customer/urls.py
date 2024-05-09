from django.urls import path
from .views import UserListCreateAPIView, UserRetrieveUpdateDestroyAPIView, UserRegisterAPIView, UserLoginAPIView
urlpatterns = [
    path('users/', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user-detail'),
    path('register/', UserRegisterAPIView.as_view(), name='user-register'),
    path('login/', UserLoginAPIView.as_view(), name='user-login'),
]
