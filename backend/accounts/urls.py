from django.urls import path
from .views import RegisterView, BlockUserView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('block/<int:pk>/', BlockUserView.as_view()),
]
