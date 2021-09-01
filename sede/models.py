from django.db import models

# Create your models here.

class SedeModel(models.Model):
    id = models.AutoField(primary_key=True)
    sede = models.CharField(max_length=120, null=False, blank=False, db_index=True)
    direccion = models.CharField(max_length=255, blank=True)
    estado = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'sedes'
        verbose_name = 'Sede'
        verbose_name_plural = 'Sedes'

    def __str__(self):
        return self.sede