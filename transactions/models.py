from django.db import models
from django.conf import settings

CATEGORY_CHOICES = [
    ("salary", "Salário"),
    ("food", "Alimentação"),
    ("rent", "Moradia"),
    ("transport", "Transporte"),
    ("other", "Outros"),
]

class Transaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    type = models.CharField(max_length=10, choices=[("income", "Receita"), ("expense", "Despesa")])

    def __str__(self):
        return f"{self.user.email} - {self.category} - {self.amount}"
