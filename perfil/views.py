from django.shortcuts import render, redirect
from django.http import HttpResponse
from perfil.models import Conta
from django.contrib import messages
from django.contrib.messages import constants
 
def home(request):
    return render(request, 'home.html')

def gerenciar(request):
    contas = Conta.objects.all()
    return render(request, 'gerenciar.html', {'contas': contas})

def cadastrar_banco(request):
    apelido = request.POST.get('apelido')
    banco = request.POST.get('banco')
    tipo = request.POST.get('tipo')
    valor = request.POST.get('valor')
    icone = request.FILES.get('icone')
    
    if len(apelido.strip()) == 0 or len(valor.strip()) == 0:
        messages.add_message(request, constants.ERROR, 'preencha todos os campos ')
        return redirect('/perfil/gerenciar/')

    conta = Conta(
        apelido = apelido,
        banco = banco,
        tipo = tipo,
        valor = valor,
        icone = icone
        
    )

    conta.save() 
    messages.add_message(request, constants.SUCCESS, 'Conta Cadastrada com sucesso')
    
    return redirect('/perfil/gerenciar/')

