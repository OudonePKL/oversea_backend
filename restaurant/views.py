from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, generics, viewsets, response
from .models import Category, Restaurant, Table, Food, FoodImages, Order, OrderItem
from .serializers import CategorySerializer
from rest_framework.generics import get_object_or_404
from django.http import Http404


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

    def get_object_or_404(self, queryset=None):
        try:
            return super().get_object()
        except Http404:
            raise Http404({"message": "Category not found"})

    def put(self, request, *args, **kwargs):
        instance = self.get_object_or_404()
        serializer = CategorySerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object_or_404()
        serializer = CategorySerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object_or_404()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
