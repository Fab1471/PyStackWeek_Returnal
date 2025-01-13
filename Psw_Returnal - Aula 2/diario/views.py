from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Pessoa

# Create your views here.
def home(request):
    return render(request, 'home.html')

def escrever(request):
    if request.method == 'GET':
        pessoas = Pessoa.objects.all()
        return render(request, 'escrever.html', {'pessoas': pessoas})
    elif request.method == 'POST':
        titulo = request.POST.get('titulo')
        tags = request.POST.getlist('tags')
        pessoas = request.POST.getlist('pessoas')
        texto = request.POST.get('texto')
        return HttpResponse(f'{titulo} - {tags} - {pessoas} - {texto}')

def cadastrar_pessoa(request):
    if request.method == 'GET':
        return render(request, 'pessoa.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        foto = request.FILES.get('foto')
        
        pessoa = Pessoa(        # a varíavel pessoa herda da Classe Pessoa que possui os 'atributos'? de nome e foto
            nome=nome,          # o primeiro é a varíavel da classe Pessoa o da esquerda e o da direita é o input que vai vir no form
            foto=foto           # o segundo é referente a variavel da função cadastrar_pessoa que vai ser recebido pelo input do form
        )
        pessoa.save()
        return redirect('escrever')
