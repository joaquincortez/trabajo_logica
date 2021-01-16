from django.db import models

# Create your models here.
class Helado(models.Model):
    nombre = models.CharField(max_length = 50)
    precio = models.DecimalField(max_digits = 6, decimal_places=2)

    def __str__(self):
        return self.nombre


class MateriaPrima(models.Model):
    nombre = models.CharField(max_length = 50)
    costo = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return self.nombre + ' ($%d)' %self.costo


class MateriaPrima_Helado(models.Model):
    helado = models.ForeignKey(Helado, on_delete=models.CASCADE)
    materia_prima = models.ForeignKey(MateriaPrima, on_delete = models.CASCADE)
    cantidad = models.IntegerField()
    porcentaje_perdida = models.FloatField()

    class Meta:
        verbose_name = 'Ingrediente'
    
    def __str__(self):
        return 'Ingrediente'