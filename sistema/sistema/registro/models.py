from django.db import models

# Create your models here.
class Persona(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100, verbose_name='nombre ')
    apellido=models.CharField(max_length=100, verbose_name='apellido ')
    imagen=models.ImageField(upload_to='imagenes/', null=True, verbose_name='imagen')
    telefono=models.CharField(max_length=100, verbose_name='telefono ')
    direccion=models.CharField(max_length=100, verbose_name='direccion ')
    
    def __str__(self) :
        fila="nombre:"+self.nombre+" || "+"apellido:"+self.apellido
        return fila
    
    def delete(self, using=None, Keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()