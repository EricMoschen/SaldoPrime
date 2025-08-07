from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'), 
    path('cadastro_usuario/', views.cadastrar_usuario, name='cadastro_usuario'),
]
