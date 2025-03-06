from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransactionViewSet, statistics_view, category_expenses_view

router = DefaultRouter()
router.register(r"transactions", TransactionViewSet, basename="transaction")

urlpatterns = [
    path('statistics/', statistics_view, name='statistics'),
    path('statistics/category-expenses/', category_expenses_view, name='category-expenses'),
    path("", include(router.urls)),
]
