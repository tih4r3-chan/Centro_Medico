from django.db import models

# Create your models here.
class Users(models.Model):
    nombre = models.CharField(max_length=100, default='DEFAULT VALUE')
    apellido = models.CharField(max_length=100, default='DEFAULT VALUE')
    email = models.CharField(max_length=100, default='DEFAULT VALUE')
    tipoUsuario = models.CharField(max_length=60, default='DEFAULT VALUE')
    password = models.CharField(max_length=100, default='DEFAULT VALUE')

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.nombre
    
    
class tipoUsuario(models.Model):
    tipo = models.CharField(max_length=100, default='DEFAULT VALUE')

    class Meta:
        db_table = 'tipoUsuario'

    def __str__(self):
        return self.tipo