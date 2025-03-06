import requests
import logging
from django.conf import settings

logger = logging.getLogger(__name__)

def get_financial_statistics(user_id, start_date, end_date, request):
    base_url = settings.GO_STATISTICS_URL  # Exemplo: "http://go-service:8080/statistics"
    
    # Extrai o token do header da requisição do Django
    headers = {}
    auth_header = request.META.get("HTTP_AUTHORIZATION")
    if auth_header:
        headers["Authorization"] = auth_header
    else:
        logger.warning("Header de autorização não encontrado na requisição.")

    params = {
        "user_id": user_id,
        "start_date": start_date,
        "end_date": end_date,
    }
    
    try:
        response = requests.get(base_url, params=params, headers=headers, timeout=5)
        if response.status_code == 200:
            return response.json()
        else:
            logger.error("Erro ao consumir o microserviço Go: %s", response.text)
    except Exception as e:
        logger.exception("Exceção na chamada do microserviço de estatísticas: %s", e)
    
    return None

def get_monthly_category_expenses(user_id, start_date, end_date, request):
    # Tenta obter uma URL específica para o endpoint ou utiliza o endpoint padrão
    base_url = getattr(settings, "GO_STATISTICS_CATEGORY_EXPENSES_URL", None)
    if not base_url:
        # Certifique-se de que esse caminho corresponde à rota registrada no microserviço Go
        base_url = settings.GO_STATISTICS_URL.rstrip("/") + "/category-expenses"

    # Extrai o token do header da requisição do Django e repassa para o microserviço
    headers = {}
    auth_header = request.META.get("HTTP_AUTHORIZATION")
    if auth_header:
        headers["Authorization"] = auth_header
    else:
        logger.warning("Header de autorização não encontrado na requisição.")

    params = {
        "user_id": user_id,
        "start_date": start_date,
        "end_date": end_date,
    }
    
    try:
        response = requests.get(base_url, params=params, headers=headers, timeout=5)
        if response.status_code == 200:
            return response.json()
        else:
            logger.error("Erro ao consumir o microserviço Go para despesas por categoria: %s", response.text)
    except Exception as e:
        logger.exception("Exceção na chamada do microserviço para despesas por categoria: %s", e)
    
    return None