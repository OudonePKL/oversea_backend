from .models import CategoryModel, RestaurantModel, FoodsModel, ImageModel, Order, OrderItem
from .serializers import CategorySerializer, RestaurantSerializer, FoodsSerializer, ImageSerializer, OrderSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, generics, viewsets, response

from .models import (
    Order,
    OrderItem,
)

from .serializers import (
    OrderSerializer,
    OrderCreateSerializer,
    OrderUpdateSerializer,
    PendingOrderSerializer,
    DoneOrderSerializer,
    ActiveOrderSerializer,
    FinishOrderSerializer,
)

class CategoryListCreate(generics.ListCreateAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

class RestaurantListCreate(generics.ListCreateAPIView):
    queryset = RestaurantModel.objects.all()
    serializer_class = RestaurantSerializer

class FoodsListCreate(generics.ListCreateAPIView):
    queryset = FoodsModel.objects.all()
    serializer_class = FoodsSerializer

class ImageListCreate(generics.ListCreateAPIView):
    queryset = ImageModel.objects.all()
    serializer_class = ImageSerializer

# Order
class OrderListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        # Retrieve orders with status "Pending"
        return Order.objects.filter(status="Pending")


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class UserOrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        return Order.objects.filter(user_id=user_id)

class OrderCreateAPIView(APIView):
    def post(self, request):
        serializer = OrderCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "success"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderUpdateAPIView(APIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    def put(self, request, pk):
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Response(
                {"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = OrderUpdateSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class OrderDeleteView(generics.DestroyAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
    
#     def delete(self, request, pk, format=None):
#         try:
#             order = Order.objects.get(pk=pk)
#         except Order.DoesNotExist:
#             return Response(
#                 {"message": "Order not found"}, status=status.HTTP_404_NOT_FOUND
#             )

#         # Delete related OrderItem instances
#         OrderItem.objects.filter(order_id=order).delete()

#         # Delete the Order instance
#         order.delete()

#         return Response({"message": "success"}, status=status.HTTP_204_NO_CONTENT)

class OrderDeleteView(generics.DestroyAPIView):
    queryset = Order.objects.all()

    def delete(self, request, pk, format=None):
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Response(
                {"message": "Order not found"}, status=status.HTTP_404_NOT_FOUND
            )

        # Delete related OrderItem instances
        OrderItem.objects.filter(order_id=order).delete()

        # Delete the Order instance
        order.delete()

        return Response({"message": "success"}, status=status.HTTP_204_NO_CONTENT)


class PendingOrderListAPIView(generics.ListAPIView):
    serializer_class = PendingOrderSerializer

    def get_queryset(self):
        store_id = self.request.query_params.get("store_id", None)
        queryset = Order.objects.filter(status="Pending")
        if store_id:
            queryset = queryset.filter(store_id=store_id)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return response.Response(
            {"count": len(serializer.data), "orders": serializer.data}
        )


class DoneOrderListAPIView(generics.ListAPIView):
    serializer_class = DoneOrderSerializer

    def get_queryset(self):
        store_id = self.request.query_params.get("store_id", None)
        queryset = Order.objects.filter(status="Done")
        if store_id:
            queryset = queryset.filter(store_id=store_id)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return response.Response(
            {"count": len(serializer.data), "orders": serializer.data}
        )


class ActiveOrderListAPIView(generics.ListAPIView):
    serializer_class = ActiveOrderSerializer

    def get_queryset(self):
        store_id = self.request.query_params.get("store_id", None)
        queryset = Order.objects.filter(status="Active")
        if store_id:
            queryset = queryset.filter(store_id=store_id)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return response.Response(
            {"count": len(serializer.data), "orders": serializer.data}
        )


class FinishOrderListAPIView(generics.ListAPIView):
    serializer_class = FinishOrderSerializer

    def get_queryset(self):
        store_id = self.request.query_params.get("store_id", None)
        queryset = Order.objects.filter(status="Finish")
        if store_id:
            queryset = queryset.filter(store_id=store_id)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return response.Response(
            {"count": len(serializer.data), "orders": serializer.data}
        )


