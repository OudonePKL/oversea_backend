from rest_framework import serializers
from .models import UserModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'email', 'password', 'is_seller', 'is_active', 'is_admin']
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        user = UserModel.objects.create_user(email=validated_data['email'], password=validated_data['password'])
        return user