from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.

produtos = [
    {   
        "id": 1,
        "img": "img/image 8.png",
        "title": "Processador AMD Ryzen 5 4600G, 3.7GHz",
        "price": "R$ 659,99",
        
    },
    {
        "id": 2,
        "img": "img/image 9.png",
        "title": "Processador AMD Ryzen 7 5700X, 3.4GHz",
        "price": "R$ 1299,99",
    },
    {
        "id": 3,
        "img": "img/image 9.png",
        "title": "Processador AMD Ryzen 5 5600, 3.5GHz",
        "price": "R$ 889,99",
    },
    {
        "id": 4,
        "img": "img/image 11.png",
        "title": "Processador Intel Core i5-10400F, 2.9GHz",
        "price": "R$ 619,99",
    },
    {
        "id": 5,
        "img": "img/image 12.png",
        "title": "Processador Intel Core i5-12400F, 2.5GHz",
        "price": "R$ 959,99",
    },
    {
        "id": 6,
        "img": "img/image 13.png",
        "title": "Processador AMD Ryzen 7 5700G, 3.8GHz",
        "price": "R$ 2299,99",
    }

]

def index(request):
    contexto = {
        'produtos': produtos
    }
    return render(request, "home.html", contexto)

def produto(request, id):
    produto = produtos[id-1]
    contexto = {
        'produto': produto
    }
    return render(request, "produto.html", contexto)

def frete(request, id):
    produto = produtos[id-1]
    contexto = {
        'produto': produto
    }
    return render(request, "frete.html", contexto)

def forma(request):
    return render(request, "forma.html",)