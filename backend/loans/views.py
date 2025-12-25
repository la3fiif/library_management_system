from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Loan
from books.models import Book

class BorrowBookView(APIView):
    def post(self, request):
        user = request.user
        book = Book.objects.get(id=request.data['book_id'])

        if book.quantity < 1:
            return Response({"error": "Not available"}, status=400)

        Loan.objects.create(user=user, book=book)
        book.quantity -= 1
        book.save()

        return Response({"message": "Book borrowed"})

class ReturnBookView(APIView):
    def post(self, request):
        loan = Loan.objects.get(id=request.data['loan_id'])
        loan.returned = True
        loan.save()

        book = loan.book
        book.quantity += 1
        book.save()

        return Response({"message": "Book returned"})
