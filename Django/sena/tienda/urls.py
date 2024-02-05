from django.urls import path

from . import views

app_name = "tienda"

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("productos/", views.productos, name="productos"),
    path("listar_categorias/", views.categorias, name="listar_categorias"),
    path("form_cat/", views.categorias_crear_formulario, name="form_cat"),
    path("categorias_guardar/", views.categorias_guardar, name="categorias_guardar"),
    path("form_edit_cat/<int:id>/", views.categorias_editar_formulario, name="form_edit_cat"),
    path("categoria_eliminar/<int:id>/", views.categoria_eliminar, name="categoria_eliminar"),
    path("cat_buscar/", views.cat_buscar, name="cat_buscar"),
    path("form_pro/", views.productos_crear_formulario, name="form_pro"),
    path("productos_guardar", views.productos_guardar, name="productos_guardar"),
    path("productos_eliminar/<int:id>/", views.productos_eliminar, name="productos_eliminar"),
    path("productos_editar/<int:id>/", views.productos_editar, name="productos_editar"),
    path("cambiar_clave/", views.cambiar_clave, name="cambiar_clave"),
    path("guardar_clave/", views.guardar_clave, name="guardar_clave"),
    path("perfil/", views.ver_perfil, name="perfil"),

    # Carrito de compra...
    path("carrito_agregar/", views.carrito_agregar, name="carrito_agregar"),
    path("carrito_listar/", views.carrito_listar, name="carrito_listar"),
    path("carrito_eliminar/<int:id>", views.carrito_eliminar, name="carrito_eliminar"),
    path("carrito_actualizar", views.carrito_actualizar, name="carrito_actualizar"),
    path("establecer_venta", views.establecer_venta, name="establecer_venta"),

    path("ventas/", views.ventas, name="venta"),
    path("ventas_usuario/", views.venta_usuario, name="venta_usuario"),
    path("detalleVenta_usuario/<int:id>", views.detalle_venta_usuarios, name="detalleVenta_usuario")
]
