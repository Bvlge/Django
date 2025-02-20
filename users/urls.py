from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import RegisterView, UserProfileView, UserDetailView, CustomTokenObtainPairView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),  # Registro de usuários
    path("token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),  # Login
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),  # Atualizar token
    path("user/", UserProfileView.as_view(), name="user_profile"),  # Perfil do usuário autenticado
    path("user/<int:pk>/", UserDetailView.as_view(), name="user_detail"),  # Buscar usuário pelo ID (Opcional)
]
