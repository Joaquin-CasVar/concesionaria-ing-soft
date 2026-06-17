from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Persona(AbstractUser):
    telefono = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'persona'
        verbose_name_plural = 'personas'

class Cliente(models.Model):
    persona = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    direccion = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.persona}"


class Vendedor(models.Model):
    persona = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    salario = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.persona}"

    class Meta:
        verbose_name = 'vendedor'
        verbose_name_plural = 'vendedores'
