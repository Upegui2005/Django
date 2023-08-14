from django.urls import path

from . import views

app_name = "tienda"

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),

    path("listar_categorias/", views.categorias, name="listar_categorias"),
    path("form_cat/", views.categorias_crear_formulario, name="form_cat"),
    path("categorias_guardar/", views.categorias_guardar, name="categorias_guardar"),
]
