from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, InventoryReportView

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = router.urls
urlpatterns += [
    path('inventory/', InventoryReportView.as_view()),
]