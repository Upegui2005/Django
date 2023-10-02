from django.contrib import admin
from django.utils.safestring import mark_safe

# Register your models here.
from .models import *


class ProductoAdmin(admin.ModelAdmin):
    fields = ["categoria", "nombre", "precio", "fecha_compra"]
    list_display = ["id", "categoria", "nombre", "precio", "fecha_compra"]
    search_fields = ["nombre", "categoria__descripcion", "categoria__nombre"]
    list_filter = ["categoria", "fecha_compra"]
    list_editable = ["nombre"]


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre", "descripcion"]
    search_fields = ["nombre", "descripcion"]


class UsuariosAdmin(admin.ModelAdmin):
    list_display = ["id", "userName", "sueldo", "nombre_completo", "rol", "verfoto"]

    def sueldo(self, obj):
        return f"${obj.id * 3}"

    def nombre_completo(self, obj):
        return mark_safe(f"<span style='color:red'> {obj.nombre} </span> {obj.apellido}")

    def verfoto(self, obj):
        try:
            return mark_safe(f"<img src='{obj.foto.url}' width='10%'>")
        except Exception as e:
            return f"Error, el archivo fue eliminado."


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Usuarios, UsuariosAdmin)
