import requests
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from django.contrib import messages

from .models import *


# Create your views here.


def login(request):
    if request.method == "POST":
        userName = Usuarios.objects.POST.get("userName")
        password = Usuarios.objects.POST.get("password")
        try:
            q = Usuarios.objects.get(userName=userName, password=password)
            messages.success(request, "Bienvenido!!")
            datos = {
                "rol": q.rol,
                "nombre": f"{q.nombre} {q.apellido}",
                "foto": q.foto.url,
                "id": q.id
            }
            request.session["sesion"] = datos
        except Usuarios.DoesNotExist:
            messages.error(request, "Usuario o contraseña no validos")
            return render(request, "tienda/login.html")
    else:
        return render(request, "tienda/login.html")


def logout(request):
    pass


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


def categoria_eliminar(request):
    return render(request, "tienda/categoria_eliminar")


def cat_buscar(request):
    render(request, "")


def productos(request):
    query = Producto.objects.all()
    contexto = {"data": query}
    return render(request, "tienda/productos/listar.html", contexto)


def productos_crear_formulario(request):
    query = Categoria.objects.all()
    contexto = {"categorias": query}
    return render(request, "tienda/productos/form_pro.html", contexto)


def productos_guardar(request):
    if request.method == "POST":
        nomb = request.POST.get("nombre")
        pre = request.POST.get("precio")
        fech = request.POST.get("fecha_compra")
        cat = Categoria.objects.get(pk=request.POST.get("categoria"))

        # insert into categoria values (null, nomb, desc)
        try:
            pro = Producto(
                nombre=nomb,
                precio=pre,
                fecha_compra=fech,
                categoria=cat
            )
            pro.save()
            messages.success(request, "Los datos fueron guardados correctamente")
        except Exception as e:
            messages.error(request, f"Error {e}")

        return HttpResponseRedirect(reverse("tienda:productos", args=()))
    else:
        try:
            q = Producto.objects.get(pk=id)
            q.nombre = nomb
            q.precio = pre
            q.fecha_compra = fech
            q.categoria = cat
            q.save()
            messages.success(request, "Actualizacion correcta")
        except Exception as e:
            messages.error(request, f"Error {e}")

    return HttpResponseRedirect(reverse("tienda:form_pro", args=()))


def productos_eliminar(request, id):
    try:
        q = Producto.objects.get(pk=id)
        q.delete()
        messages.success(request, "Registro eliminado")
    except Exception as e:
        messages.error(request, "Errror {e}")
    return HttpResponseRedirect(reverse("tienda:productos", args=()))


def productos_editar(request, id):
    q = Producto.objects.get(pk=id)
    query = Categoria.objects.all()
    contexto = {"id": id, "data": q, "categorias": query}
    return render(request, "tienda/productos/form_pro.html", contexto)
