from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.urls import reverse
def logout_view(request):
    logout(request)  
    return redirect('login')  

# Login 

def login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username).first()
        if user and user.check_password(password):
            messages.success(request, 'Login realizado com sucesso.')
            return redirect('dashboard')  

    return render(request, 'login.html')


# Cadastro de usuário

def cadastrar_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, 'As senhas não coincidem.')
            return render(request, 'cadastro.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Nome de usuário já existe.')
            return render(request, 'cadastro.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'E-mail já está em uso.')
            return render(request, 'cadastro.html')

        User.objects.create_user(username=username, email=email, password=password1)
        messages.success(request, 'Usuário cadastrado com sucesso.')
        return redirect('login')

    return render(request, 'cadastro.html')


# Recuperação de senha

def recuperacao_senha(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()

        if user:
            # Gera token para o usuário
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))

            # Cria link para resetar senha (ajuste a URL conforme seu projeto)
            reset_url = request.build_absolute_uri(
                reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token})
            )

            # Renderiza o corpo do e-mail com template (opcional)
            message = render_to_string('emails/reset_password_email.html', {
                'user': user,
                'reset_url': reset_url,
            })

            # Envia e-mail (configure seu EMAIL_HOST etc no settings.py)
            send_mail(
                subject='Recuperação de senha - SaldoPrime',
                message=message,
                from_email='noreply@saldoprime.com',
                recipient_list=[email],
                fail_silently=False,
            )

            messages.success(request, 'Instruções para recuperação de senha enviadas para o seu e-mail.')
        else:
            messages.error(request, 'E-mail não encontrado.')

    return render(request, 'login.html')