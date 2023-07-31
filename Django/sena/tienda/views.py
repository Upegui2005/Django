from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, "tienda/index.html")


def login(request):
    return HttpResponse("Login")


def productos(request):
    return render(request, "tienda/productos.html")
