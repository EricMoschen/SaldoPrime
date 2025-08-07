# menuos/models.py

from django.db import models

class ReceitasDespesas(models.Model):
    TIPO_CHOICES = [
        ('receita', 'Receita'),
        ('despesa', 'Despesa'),
    ]

    METODO_PAGAMENTO_CHOICES = [
        ('Pix', 'Pix'),
        ('Débito', 'Débito'),
        ('Crédito', 'Crédito'),
    ]

    tipo_conta = models.CharField(max_length=10, choices=TIPO_CHOICES)
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_vencimento = models.DateField()

    # Campos só para receita
    tipo_receita = models.CharField(max_length=50, blank=True, null=True)

    # Campos só para despesa
    metodo_pagamento = models.CharField(max_length=10, choices=METODO_PAGAMENTO_CHOICES, blank=True, null=True)
    total_parcelas = models.PositiveIntegerField(default=1)
    valor_parcela = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.get_tipo_conta_display()} - {self.descricao} - R$ {self.valor}"
