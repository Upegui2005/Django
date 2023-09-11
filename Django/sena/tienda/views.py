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
    result = Categoria.objects.all()
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
            cat = Categoria(
                nombre=nomb,
                descripcion=desc
            )
            cat.save()
            messages.success(request, "Los datos fueron guardados correctamente")
        except Exception as e:
            messages.error(request, f"Error {e}")

        return HttpResponseRedirect(reverse("tienda:listar_categorias", args=()))
    else:
        messages.error(request, "No se enviaron datos...")
        return HttpResponseRedirect(reverse("tienda:form_cat", args=()))


def categorias_editar_formulario(request, id):
    q = Categoria.objects.get(pk=id)
    contexto = {"id": id, "data": q}
    return render(request, "tienda/categoria/cat-form.html", contexto)


def login():
    return HttpResponse("Login")


def logout(request):
    return render(request, "tienda/logout.html")
