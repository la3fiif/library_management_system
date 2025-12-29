from django.urls import path
from .views import RegisterView, BlockUserView, UserDetailView, UserListView

urlpatterns = [
    path('', UserListView.as_view()),
    path('register/', RegisterView.as_view()),
    path('<int:pk>/', UserDetailView.as_view()),
    path('block/<int:pk>/', BlockUserView.as_view()),
]
