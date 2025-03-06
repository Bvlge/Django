import requests
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Transaction
from .serializers import TransactionSerializer
from .services.statistics_service import get_financial_statistics, get_monthly_category_expenses
from datetime import datetime
from drf_spectacular.utils import extend_schema, OpenApiParameter


class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filtra as transações apenas do usuário autenticado
        return Transaction.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Atribui o usuário autenticado à transação criada
        serializer.save(user=self.request.user)


@extend_schema(
    parameters=[
        OpenApiParameter(
            name="start_date",
            description="Data inicial no formato YYYY-MM-DD",
            required=False,
            type=str
        ),
        OpenApiParameter(
            name="end_date",
            description="Data final no formato YYYY-MM-DD",
            required=False,
            type=str
        ),
    ],
    responses={200: "Retorna as estatísticas financeiras"},
)
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def statistics_view(request):
    """
    Obtém estatísticas financeiras do microserviço Go.
    O usuário autenticado fornece o token dinâmico.
    """
    user_id = request.user.id
    start_date = request.GET.get("start_date", "1970-01-01")
    end_date = request.GET.get("end_date")
    
    # Aqui é passado o objeto request como argumento, conforme esperado pela função.
    stats = get_financial_statistics(user_id, start_date, end_date, request)

    if stats is None:
        return Response({"error": "Erro ao obter estatísticas"}, status=500)
    
    return Response(stats)


@extend_schema(
    parameters=[
        OpenApiParameter(
            name="start_date",
            description="Data inicial no formato YYYY-MM-DD",
            required=False,
            type=str
        ),
        OpenApiParameter(
            name="end_date",
            description="Data final no formato YYYY-MM-DD",
            required=False,
            type=str
        ),
    ],
    responses={200: "Retorna as estatísticas mensais de despesas por categoria"},
)
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def category_expenses_view(request):
    """
    Obtém a média mensal de despesas por categoria do microserviço Go.
    O usuário autenticado fornece o token dinâmico.
    """
    user_id = request.user.id
    start_date = request.GET.get("start_date", "2023-01-01")
    end_date = request.GET.get("end_date", datetime.now().strftime("%Y-%m-%d"))

    stats = get_monthly_category_expenses(user_id, start_date, end_date, request)

    if stats is None:
        return Response({"error": "Erro ao obter estatísticas de despesas por categoria"}, status=500)
    
    return Response(stats)