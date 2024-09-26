from django.db import models


class Libro(models.Model):
    id_libro = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=99)
    autor = models.CharField(max_length=99)
    año_publicacion = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    copias = models.IntegerField(default=0)

    class Meta:
        db_table = 'LIBROS'

    def __str__(self):
        return self.titulo

