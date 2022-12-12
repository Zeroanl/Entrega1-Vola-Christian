from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    altura = models.FloatField(default=0.0)

    class Meta:
        verbose_name="persona"
        verbose_name_plural="personas"

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Mascota(models.Model):
    clase_animal = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    dueño = models.ForeignKey(Persona, on_delete=models.CASCADE)

    class Meta:
        verbose_name="mascota"
        verbose_name_plural="mascotas"

class Trabajo(models.Model):
    tipo_trabajo = models.CharField(max_length=100)
    trabajo = models.CharField(max_length=100)
    trabajador = models.ForeignKey(Persona, on_delete=models.CASCADE)

    class Meta:
        verbose_name="trabajo"
        verbose_name_plural="trabajos"