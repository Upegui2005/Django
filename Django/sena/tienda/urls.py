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
]
