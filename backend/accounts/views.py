from rest_framework import generics
from .models import User
from .serializers import UserSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BlockUserView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
