from django.db import models


# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.id} ----- {self.nombre}"


class Producto(models.Model):
    nombre = models.CharField(max_length=254)
    precio = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    fecha_compra = models.DateField()

    def __str__(self):
        return f"{self.id} ----- {self.nombre} ----- {self.precio}"
