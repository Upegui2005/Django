from django.contrib import admin

# Register your models here.
from .models import Categoria, Producto


class ProductoAdmin(admin.ModelAdmin):
    fields = ["categoria", "nombre", "precio", "fecha_compra"]
    list_display = ["id", "categoria", "nombre", "precio", "fecha_compra"]
    search_fields = ["nombre", "categoria__descripcion", "categoria__nombre"]
    list_filter = ["categoria", "fecha_compra"]
    list_editable = ["nombre"]


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre", "descripcion"]
    search_fields = ["nombre", "descripcion"]


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
