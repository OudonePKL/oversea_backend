from .models import UserModel
from .serializers import UserSerializer
from rest_framework import generics, permissions, status
from rest_framework.response import Response

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

class UserRegisterAPIView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

class UserLoginAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = UserModel.objects.filter(email=email).first()

        if user and user.check_password(password):
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
