from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from loans.models import Loan

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class InventoryReportView(APIView):
    def get(self, request):
        books = Book.objects.all().count()
        borrowed = Loan.objects.filter(returned=False).count()

        return Response({
            "total_books": books,
            "borrowed_books": borrowed,
            "available_books": books - borrowed
        })