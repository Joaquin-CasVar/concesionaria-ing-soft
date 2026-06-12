from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class TipoCombustible(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class TipoTransmision(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class TipoDireccion(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Color (models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Auto(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    combustible = models.ForeignKey(TipoCombustible, on_delete=models.CASCADE)
    transmision = models.ForeignKey(TipoTransmision, on_delete=models.CASCADE)
    direccion = models.ForeignKey(TipoDireccion, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    turbo = models.BooleanField(default=False)
    anio = models.IntegerField()
    nuevo = models.BooleanField(default=True)
    kilometros = models.IntegerField(default=0)
    patente = models.CharField(max_length=20, null=True, blank=True)
    puertas = models.IntegerField(default=4)
    marchas = models.IntegerField(default=5)
    foto = models.ImageField(upload_to='autos/', null=True, blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.marca} {self.nombre} ({self.anio})"
    
    class Meta:
        ordering = ['-id']
