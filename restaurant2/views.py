from django.shortcuts import render
from .models import Category, Restaurant, Table, MenuItem, Order, OrderItem
from .serializers import (
    CategorySerializer,
    RestaurantSerializer, RestaurantManageSerializer,
    TableSerializer, MenuItemSerializer, OrderSerializer, OrderItemSerializer
)
from django.http import Http404
from rest_framework import generics, status, filters, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action


# Category management
class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def post(self, request, *args, **kwargs):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "success"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_object(self, queryset=None):
        try:
            return super().get_object()
        except Http404:
            raise Http404({"message": "Category not found"})

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CategorySerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CategorySerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Restaurant management
class RestaurantList(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    
class RestaurantRetrieve(generics.RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    
    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise Http404({"message": "Food not found"})


# class TableViewSet(viewsets.ModelViewSet):
#     queryset = Table.objects.all()
#     serializer_class = TableSerializer

#     @action(detail=True, methods=["get"])
#     def availability(self, request, pk=None):
#         table = self.get_object()
#         available = table.is_available()
#         return Response({"available": available})

class TableViewSet(viewsets.ModelViewSet):
    serializer_class = TableSerializer

    def get_queryset(self):
        restaurant_id = self.request.query_params.get('restaurant_id')
        if restaurant_id:
            return Table.objects.filter(restaurant_id=restaurant_id)
        else:
            return Table.objects.all()

    @action(detail=True, methods=["get"])
    def availability(self, request, pk=None):
        table = self.get_object()
        available = table.is_available()
        return Response({"available": available})


# class MenuItemViewSet(viewsets.ModelViewSet):
#     queryset = MenuItem.objects.all()
#     serializer_class = MenuItemSerializer

class MenuItemViewSet(viewsets.ModelViewSet):
    serializer_class = MenuItemSerializer
    
    def get_queryset(self):
        restaurant_id = self.request.query_params.get('restaurant_id')
        if restaurant_id:
            return MenuItem.objects.filter(restaurant_id=restaurant_id)
        else:
            return MenuItem.objects.all()


# class OrderViewSet(viewsets.ModelViewSet):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer

#     def perform_create(self, serializer):
#         serializer.save()

#     def perform_update(self, serializer):
#         serializer.save()

#     @action(detail=True, methods=["get"])
#     def status(self, request, pk=None):
#         order = self.get_object()
#         return Response({"status": order.status})

#     @action(detail=True, methods=["patch"])
#     def update_status(self, request, pk=None):
#         order = self.get_object()
#         new_status = request.data.get("status")
#         if new_status in dict(Order.STATUS_CHOICES):
#             order.status = new_status
#             order.save()
#             return Response({"status": order.status})
#         else:
#             return Response(
#                 {"error": "Invalid status"}, status=status.HTTP_400_BAD_REQUEST
#             )

#     @action(detail=True, methods=["get"])
#     def payment_status(self, request, pk=None):
#         order = self.get_object()
#         return Response({"paid": order.paid})

#     @action(detail=True, methods=["patch"])
#     def make_paid(self, request, pk=None):
#         order = self.get_object()
#         order.paid = True
#         order.save()
#         return Response({"paid": order.paid})

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    
    def get_queryset(self):
        restaurant_id = self.request.query_params.get('restaurant_id')
        if restaurant_id:
            return Order.objects.filter(restaurant_id=restaurant_id)
        else:
            return Order.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    @action(detail=True, methods=["get"])
    def status(self, request, pk=None):
        order = self.get_object()
        return Response({"status": order.status})

    @action(detail=True, methods=["patch"])
    def update_status(self, request, pk=None):
        order = self.get_object()
        new_status = request.data.get("status")
        if new_status in dict(Order.STATUS_CHOICES):
            order.status = new_status
            order.save()
            return Response({"status": order.status})
        else:
            return Response(
                {"error": "Invalid status"}, status=status.HTTP_400_BAD_REQUEST
            )

    @action(detail=True, methods=["get"])
    def payment_status(self, request, pk=None):
        order = self.get_object()
        return Response({"paid": order.paid})

    @action(detail=True, methods=["patch"])
    def make_paid(self, request, pk=None):
        order = self.get_object()
        order.paid = True
        order.save()
        return Response({"paid": order.paid})


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
