from django.shortcuts import render, redirect
from perfil.models import Categoria, Conta
from .models import Valores
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages import constants
from datetime import datetime
 
# Create your views here.
def novo_valor(request):
    if request.method == 'GET':
        contas = Conta.objects.all()
        categorias = Categoria.objects.all()
        return render(request, 'novo_valor.html', {'contas': contas, 'categorias': categorias})
        
    elif request.method == "POST":
        valor = request.POST.get('valor')
        categoria = request.POST.get('categoria')
        descricao = request.POST.get('descricao')
        data = request.POST.get('data')
        conta = request.POST.get('conta')
        tipo = request.POST.get('tipo') 

        valores = Valores(
            valor=valor,
            categoria_id=categoria,
            descricao=descricao,
            data=data,
            conta_id=conta,
            tipo=tipo,

        )
        valores.save()

        conta = Conta.objects.get(id=conta)
        if tipo == 'E':
            conta.valor += int(valor)
        else:
            conta.valor -= int(valor)
        conta.save()
    
        messages.add_message(request, constants.SUCCESS, 'entrada/saida cadastrada com sucesso!')
        return redirect('/extrato/novo_valor')

def view_extrato(request):
    contas = Conta.objects.all()
    categorias = Categoria.objects.all()
    conta_get = request.GET.get('conta')
    categoria_get = request.GET.get('categoria')
    

    valores = Valores.objects.filter(data__month=datetime.now().month)

     
    if conta_get:
        valores = valores.filter(conta_id=conta_get)
    if categoria_get:
        valores = valores.filter(categoria_id=categoria_get)
      
    return render(request, 'view_extrato.html', {'valores': valores, 'contas': contas, 'categorias': categorias})