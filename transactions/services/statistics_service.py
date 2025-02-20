import requests
from django.conf import settings

def get_financial_statistics(user_id, start_date, end_date, request):
    base_url = settings.GO_STATISTICS_URL  # Exemplo: "http://go-service:8080/statistics"
    
    # Extrair o token do header da requisição do Django
    headers = {}
    auth_header = request.META.get("HTTP_AUTHORIZATION")
    if auth_header:
        headers["Authorization"] = auth_header

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
            print("Erro ao consumir o microserviço Go:", response.text)
    except Exception as e:
        print("Exceção na chamada do microserviço de estatísticas:", e)
    
    return None
