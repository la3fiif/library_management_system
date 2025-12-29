from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import BookCreateView, BookDeleteView, BookUpdateView, BookViewSet, InventoryReportView

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = router.urls
urlpatterns += [
    path('inventory/', InventoryReportView.as_view()),
    path('books/add/', BookCreateView.as_view(), name='book-add'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]