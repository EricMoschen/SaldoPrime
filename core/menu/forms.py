# menuos/forms.py

from django import forms
from .models import ReceitasDespesas

class ReceitasDespesasForm(forms.ModelForm):
    class Meta:
        model = ReceitasDespesas
        fields = [
            'tipo_conta', 'descricao', 'valor', 'data_vencimento',
            'tipo_receita', 'metodo_pagamento', 'total_parcelas', 'valor_parcela'
        ]

        widgets = {
            'data_vencimento': forms.DateInput(attrs={'type': 'date'}),
            'valor_parcela': forms.NumberInput(attrs={'readonly': 'readonly'}),
        }
