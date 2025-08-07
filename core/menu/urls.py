from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('receitas_despesas/', views.receitas_despesas, name='receitas_despesas'),
    path('contas_futuras/', views.contas_futuras, name='contas_futuras'),
    path('relatorios/', views.relatorios, name='relatorios'),
    path('configuracoes/', views.configuracoes, name='configuracoes'),
]
