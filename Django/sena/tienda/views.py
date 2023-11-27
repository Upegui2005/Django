import requests
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from django.contrib import messages

from .models import *


# Create your views here.


def login(request):
    if request.method == "POST":
        userName = request.POST.get("userName")
        password = request.POST.get("password")
        try:
            q = Usuarios.objects.get(userName=userName, password=password)
            messages.success(request, "Bienvenido!!")
            datos = {
                "rol": q.rol,
                "nombre_rol": q.get_rol_display(),
                "nombre": f"{q.nombre} {q.apellido}",
                "foto": q.foto.url if q.foto else "media/fotos/default.png",
                "id": q.id
            }
            request.session["logueo"] = datos
            return HttpResponseRedirect(reverse("tienda:index"))

        except Usuarios.DoesNotExist:
            messages.error(request, "Usuario o contraseña no validos")
            return render(request, "tienda/login.html")
    else:
        if request.session.get("logueo", False):
            return HttpResponseRedirect(reverse("tienda:index"))
        else:
            return render(request, "tienda/login.html")


def logout(request):
    try:
        del request.session["logueo"]
        del request.session["carrito"]
        messages.success(request, "Sesion cerrada correctamente")
    except Exception as e:
        messages.error(request, f"Error: {e}")
    return HttpResponseRedirect(reverse("tienda:login"))


def index(request):
    if request.session.get("logueo", False):
        c = Categoria.objects.all()

        # Detectar si viene paramétro id categoría para filtrar o no...
        filtro_categoria = request.GET.get("id")

        if filtro_categoria != None and filtro_categoria != '0':
            p = Producto.objects.filter(categoria_id=filtro_categoria)
            request.session["submenu"] = int(filtro_categoria)
        else:
            p = Producto.objects.all()
            request.session["submenu"] = 0

        contexto = {"categorias": c, "productos": p}
        return render(request, "tienda/index.html", contexto)
    else:
        return HttpResponseRedirect(reverse("tienda:login"))


def categorias(request):
    sesion = request.session.get("logueo", False)
    if sesion["nombre_rol"] != "Usuario":
        result = Categoria.objects.all()
        context = {"data": result}
        return render(request, "tienda/categoria/listar.html", context)
    else:
        messages.warning(request, "Te crees hacker e intentas eso, sos un pequeñin")
        return HttpResponseRedirect(reverse("tienda:index"))


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


def cambiar_clave(request):
    return render(request, "tienda/usuarios/cambio_clave.html")


def guardar_clave(request):
    usuario = request.session.get("logueo", False)
    if usuario:
        if request.method == "POST":
            actual = request.POST.get("actual")
            clave1 = request.POST.get("clave1")
            clave2 = request.POST.get("clave2")
            try:
                q = Usuarios.objects.get(pk=usuario["id"], password=actual)
                if clave1 == clave2:
                    q.password = clave1
                    q.save()
                    messages.success(request, "Contraseña cambiada correctamente")
                    return HttpResponseRedirect(reverse("tienda:cambiar_clave"))
                else:
                    messages.warning(request, "Nuevas contraseñas no coinciden")
                    return HttpResponseRedirect(reverse("tienda:cambiar_clave", kwargs={'actual': actual}))
            except Exception as e:
                messages.warning(request, "Contraseña no valida...")
                return HttpResponseRedirect(reverse("tienda:cambiar_clave"))
    else:
        return HttpResponseRedirect(reverse("tienda:logueo"))


def ver_perfil(request):
    usuario = request.session.get("logueo", False)
    q = Usuarios.objects.get(pk=usuario["id"])
    contexto = {"data": q}
    return render(request, "tienda/usuarios/perfil.html", contexto)


def carrito_agregar(request):
    if request.method == "POST":
        id_producto = request.POST.get("id")
        cantidad = int(request.POST.get("cantidad"))

        if not request.session.get("carrito", False):
            request.session["carrito"] = []

        carrito = request.session.get("carrito", False)

        encontrado = False
        for p in carrito:
            if p["id"] == id_producto:
                encontrado = True
                p["cantidad"] += cantidad
                messages.success(request, "Producto ya en carrito, se incremeto la cantidad!")
                break

        if not encontrado:
            carrito.append({"id": id_producto, "cantidad": cantidad})
            messages.success(request, "Producto agregado")

        request.session["carrito"] = carrito
        print(carrito)

    else:
        messages.warning(request, "No se enviaron datos...")
    return redirect("tienda:index")


def carrito_listar(request):
    carrito = request.session.get("carrito", False)

    if carrito:
        for p in carrito:
            query = Producto.objects.get(pk=p["id"])
            p["nombre"] = query.nombre
            p["precio"] = query.precio
            p["foto"] = query.foto.url

    contexto = {"datos": carrito}

    return render(request, "tienda/carrito/listar_carrito.html", contexto)
