from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30, unique=True)
    correo = models.EmailField()

    def __str__(self):
        return "%s %s %s %s" % (self.nombre,
                self.apellido,
                self.cedula,
                self.correo)

    def get_provincia(self):
        """
        """
        dato = self.cedula[0:2]
        valor = "Sin Provincia"
        if dato == "11":
            valor = "Loja"
        else:
            if dato == "17":
                valor = "Pichincha"
        return valor
    
    def get_gasto_telefonos(self):
        costo_por_telefono = 14
        cantidad_telefonos = self.numeros_telefonicos.count()
        return cantidad_telefonos * costo_por_telefono

class NumeroTelefonico(models.Model):
    telefono = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)

    valor_mensual = models.FloatField(
        default=0.0,
        db_default=0.0,
        null=False,
        blank=False
    )

    estudiante = models.ForeignKey(
        Estudiante,
        on_delete=models.CASCADE,
        related_name="numeros_telefonicos"
    )

    def __str__(self):
        return "%s %s" % (
            self.telefono,
            self.tipo
        )