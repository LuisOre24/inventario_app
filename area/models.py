from django.db import models

# Create your models here.


class AreaModel(models.Model):
    id = models.AutoField(primary_key=True)
    area = models.CharField(max_length=120, null=False, blank=False, db_index=True)
    estado = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'areas'
        verbose_name = 'Area'
        verbose_name_plural = 'Areas'

    def __str__(self):
        return self.area