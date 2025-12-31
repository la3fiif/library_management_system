from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from accounts.models import User

from .serializers import LoanSerializer
from .models import Loan
from books.models import Book

class LoanListView(generics.ListAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

class LoanDeleteView(generics.DestroyAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

@method_decorator(csrf_exempt, name='dispatch')
class BorrowBookView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        user_id = request.data['user_id']
        book_id = request.data['book_id']

        user = User.objects.get(id=user_id)
        book = Book.objects.get(id=book_id)

        if book.quantity < 1:
            return Response({"error": "Not available"}, status=400)

        Loan.objects.create(user=user, book=book)
        book.quantity -= 1
        book.save()

        return Response({"message": "Book borrowed"})


@method_decorator(csrf_exempt, name='dispatch')
class ReturnBookView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        loan_id = request.data['loan_id']
        loan = Loan.objects.get(id=loan_id)

        if loan.returned:
            return Response({"error": "Already returned"}, status=400)

        loan.returned = True
        loan.save()

        book = loan.book
        book.quantity += 1
        book.save()

        return Response({"message": "Book returned"})
