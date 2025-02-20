from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransactionViewSet, statistics_view

router = DefaultRouter()
router.register(r"transactions", TransactionViewSet, basename="transaction")

urlpatterns = [
    path('statistics/', statistics_view, name='statistics'),
    path("", include(router.urls)),
]
