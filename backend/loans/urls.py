from django.urls import path
from .views import BorrowBookView, ReturnBookView

urlpatterns = [
    path('borrow/', BorrowBookView.as_view()),
    path('return/', ReturnBookView.as_view()),
]
