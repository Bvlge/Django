# Generated by Django 5.1.6 on 2025-02-19 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(choices=[('salary', 'Salário'), ('food', 'Alimentação'), ('rent', 'Moradia'), ('transport', 'Transporte'), ('other', 'Outros')], max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('date', models.DateField()),
                ('type', models.CharField(choices=[('income', 'Receita'), ('expense', 'Despesa')], max_length=10)),
            ],
        ),
    ]
