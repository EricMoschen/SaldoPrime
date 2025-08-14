
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('menu.urls')),
    path('usuario/', include('usuario.urls')),
    
    # Reset de senha
    path('usuario/password_reset/', auth_views.PasswordResetView.as_view(
    template_name='recuperar_senha.html',                      # template do formulário (onde usuário digita o e-mail)
    email_template_name='email_recuperacao.html',  # template do corpo do e-mail enviado
), name='password_reset'),
    path('usuario/password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='email_recuperacao_enviado.html'), name='password_reset_done'),
    path('usuario/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='confirmar_recuperacao.html'), name='password_reset_confirm'),
    path('usuario/reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='recuperacao_concluida.html'), name='password_reset_complete'),
]
