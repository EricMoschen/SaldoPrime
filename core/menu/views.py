from django.shortcuts import render, redirect
from .forms import ReceitasDespesasForm

# Create your views here.
def dashboard(request):
    return render(request, 'menu/dashboard.html')



def contas_futuras(request):
    return render(request, 'menu/contas_futuras.html')

def relatorios(request):
    return render(request, 'menu/relatorios.html')

def configuracoes(request):
    return render(request, 'menu/configuracoes.html')


# Função para lidar com receitas e despesas
def receitas_despesas(request):
    if request.method == 'POST':
        form = ReceitasDespesasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('receitas_despesas')  
    else:
        form = ReceitasDespesasForm()

    return render(request, 'menu/receitas_despesas.html', {'form': form})