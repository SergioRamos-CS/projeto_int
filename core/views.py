from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Cliente, Obra
from .forms import ClienteForm, ObraForm
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Credenciais inválidas'})
    return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    return render(request, 'home.html')

# Views para Clientes
@login_required
def clientes(request):
    clientes_list = Cliente.objects.all().order_by('nome')
    context = {'clientes': clientes_list}
    return render(request, 'clientes/clientes.html', context)

@login_required
def add_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente cadastrado com sucesso!')
            return redirect('clientes')
        else:
            messages.error(request, 'Corrija os erros no formulário')
    else:
        form = ClienteForm()
    
    return render(request, 'clientes/add_cliente.html', {'form': form})

@login_required
def edit_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
    
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente atualizado com sucesso!')
            return redirect('clientes')
    else:
        form = ClienteForm(instance=cliente)
    
    return render(request, 'clientes/edit_cliente.html', {'form': form, 'cliente': cliente})

@login_required
def delete_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
    
    if request.method == 'POST':
        cliente.delete()
        messages.success(request, 'Cliente excluído permanentemente!')
        return redirect('clientes')
    
    return render(request, 'confirm_delete.html', {'object': cliente})

# Views para Obras
@login_required
def obras(request):
    obras_list = Obra.objects.all().select_related('cliente').order_by('-data_inicio')
    context = {'obras': obras_list}
    return render(request, 'obras/obras.html', context)

@login_required
def add_obra(request):
    if request.method == 'POST':
        form = ObraForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Obra cadastrada com sucesso!')
            return redirect('obras')
        else:
            messages.error(request, 'Erro no formulário. Verifique os dados.')
    else:
        form = ObraForm()
    
    return render(request, 'obras/add_obra.html', {'form': form})

@login_required
def edit_obra(request, id_obra):
    obra = get_object_or_404(Obra, id_obra=id_obra)
    
    if request.method == 'POST':
        form = ObraForm(request.POST, instance=obra)
        if form.is_valid():
            form.save()
            messages.success(request, 'Obra atualizada com sucesso!')
            return redirect('obras')
    else:
        form = ObraForm(instance=obra)
    
    return render(request, 'obras/edit_obra.html', {'form': form, 'obra': obra})

@login_required
def delete_obra(request, id_obra):
    obra = get_object_or_404(Obra, id_obra=id_obra)
    
    if request.method == 'POST':
        obra.delete()
        messages.success(request, 'Obra excluída permanentemente!')
        return redirect('obras')
    
    return render(request, 'confirm_delete.html', {'object': obra})