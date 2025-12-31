from django.urls import path
from django.views.generic import TemplateView
from .views import BorrowBookView, LoanDeleteView, LoanListView, ReturnBookView

urlpatterns = [
    path('', LoanListView.as_view()),
    path('<int:pk>/', LoanDeleteView.as_view()),
    path('borrow/', BorrowBookView.as_view()),
    path('return/', ReturnBookView.as_view()),
    path('user/', TemplateView.as_view(template_name='user.html')),
]
