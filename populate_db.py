import os
import django
from random import choice, uniform
from django.utils.timezone import now, timedelta

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from users.models import CustomUser
from transactions.models import Transaction

# Função para criar usuários
def create_users():
    users = [
        {"email": "user1@example.com", "name": "João Silva"},
        {"email": "user2@example.com", "name": "Ana Souza"},
        {"email": "user3@example.com", "name": "Carlos Lima"},
    ]
    user_objects = []
    for user in users:
        user_obj, created = CustomUser.objects.get_or_create(
            email=user["email"],
            defaults={
                "name": user["name"],
                "is_active": True,
            }
        )
        user_obj.set_password("senha123")
        user_obj.save()
        user_objects.append(user_obj)
    return user_objects

# Função para criar transações
def create_transactions(users):
    categories = ["Salary", "Food", "Rent", "Transport", "Other"]
    types = ["Income", "Loss"]
    for user in users:
        for _ in range(10):
            Transaction.objects.create(
                user=user,
                amount=round(uniform(50, 5000), 2),
                category=choice(categories),
                description=f"Transação de {user.name}",
                date=now().date() - timedelta(days=choice(range(1, 365))),
                type=choice(types),
            )

def main():
    users = [
        {"email": "user1@example.com", "name": "João Silva"},
        {"email": "user2@example.com", "name": "Ana Souza"},
        {"email": "user3@example.com", "name": "Carlos Lima"},
    ]
    create_transactions(users)
    print("Banco de dados populado com sucesso!")

if __name__ == "__main__":
    main()
