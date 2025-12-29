from rest_framework import viewsets, generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import AllowAny

from loans.models import Loan
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]

class InventoryReportView(APIView):
    def get(self, request):
        books = Book.objects.all().count()
        borrowed = Loan.objects.filter(returned=False).count()

        return Response({
            "total_books": books,
            "borrowed_books": borrowed,
            "available_books": books - borrowed
        })
    
@method_decorator(csrf_exempt, name='dispatch')
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]  

@method_decorator(csrf_exempt, name='dispatch')
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]

@method_decorator(csrf_exempt, name='dispatch')
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]