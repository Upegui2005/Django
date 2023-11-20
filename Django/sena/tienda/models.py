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
    stock = models.IntegerField(default=1)
    foto = models.ImageField(null=True, blank=True, default='fotos_productos/default.png', upload_to='fotos_productos')

    def __str__(self):
        return f"{self.id} ----- {self.nombre} ----- {self.precio}"


class Usuarios(models.Model):
    ROLES = (
        (1, 'Administrador'),
        (2, 'WebMaster'),
        (3, 'Usuario'),
    )
    foto = models.ImageField(null=True, blank=True, default='fotos/default.png', upload_to='fotos')
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    userName = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    rol = models.IntegerField(choices=ROLES, default=3)

    def __str__(self):
        return f"{self.userName}"
