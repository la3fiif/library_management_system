from django.urls import path
from .views import BorrowBookView, LoanDeleteView, LoanListView, ReturnBookView

urlpatterns = [
    path('', LoanListView.as_view()),
    path('<int:pk>/', LoanDeleteView.as_view()),
    path('borrow/', BorrowBookView.as_view()),
    path('return/', ReturnBookView.as_view()),
]
