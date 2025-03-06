from django.db import models
from django.conf import settings

CATEGORY_CHOICES = [
    ("Salary", "Salário"),
    ("Food", "Alimentação"),
    ("Rent", "Moradia"),
    ("Transport", "Transporte"),
    ("Other", "Outros"),
]

TYPE_CHOICES = [
    ("Income", "Receita"),
    ("Receita", "Receita"),
    ("Loss", "Despesa"),
    ("Despesa", "Despesa"),
]

class Transaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)

    def __str__(self):
        return f"{self.user.email} - {self.category} - {self.amount}"

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(type__in=["Income", "Receita", "Loss", "Despesa"]),
                name="check_transaction_type"
            )
        ]