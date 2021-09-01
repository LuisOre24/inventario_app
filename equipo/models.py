from django.db import models
from sede.models import SedeModel
from area.models import AreaModel
# Create your models here.

class EquipoModel(models.Model):
    id = models.AutoField(primary_key=True)
    sede = models.ForeignKey(SedeModel, on_delete=models.CASCADE, null=True)
    area = models.ForeignKey(AreaModel, on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=120)
    procesador = models.CharField(max_length=120)
    ram = models.CharField(max_length=120)
    almacenamiento = models.CharField(max_length=120)
    monitor = models.CharField(max_length=120)
    teclado = models.CharField(max_length=120)
    mouse = models.CharField(max_length=120)
    printer1 = models.CharField(max_length=120)
    printer2 = models.CharField(max_length=120)
    estado = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'equipos'
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'

    def __str__(self):
        return f'{self.nombre}-{self.procesador}-{self.ram}-{self.almacenamiento}'
        