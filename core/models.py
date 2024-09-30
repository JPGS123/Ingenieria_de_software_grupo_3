from django.db import models


class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=99)

    class Meta:
        db_table = 'CATEGORIAS'

    def __str__(self):
        return self.nombre_categoria


class Libro(models.Model):
    id_libro = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=99)
    autor = models.CharField(max_length=99)
    año_publicacion = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    copias = models.IntegerField(default=0)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, db_column='ID_CATEGORIA', default=1)

    class Meta:
        db_table = 'LIBROS'

    def __str__(self):
        return self.titulo
    




