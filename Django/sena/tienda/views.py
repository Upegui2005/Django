import requests
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from django.contrib import messages

from .models import Categoria, Producto


# Create your views here.


def index(request):
    return render(request, "tienda/index.html")


def categorias(request):
    result = Categoria.objects.all
    context = {"data": result}
    return render(request, "tienda/categoria/listar.html", context)


def categorias_crear_formulario(request):
    return render(request, "tienda/categoria/cat-form.html")


def categorias_guardar(request):
    if request.method == "POST":
        nomb = request.POST.get("nombre")
        desc = request.POST.get("descripcion")
        # insert into categoria values (null, nomb, desc)
        try:
            q = Categoria(
                nombre=nomb,
                descripcion=desc
            )
            q.save()
            messages.success(request, "Los datos fueron guardados correctamente")
        except Exception as e:
            messages.warning(request, f"Error {e}")

            return HttpResponseRedirect(reverse("tienda:listar_categorias", args=()))
    else:
        return HttpResponse("No se enviaron datos...")


def login():
    return HttpResponse("Login")


def logout(request):
    return render(request, "tienda/logout.html")
