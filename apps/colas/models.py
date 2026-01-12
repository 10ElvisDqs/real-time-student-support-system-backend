from django.db import models

class Cola(models.Model):
    nombre = models.CharField(max_length=100)  # Ej: "Caja", "Inscripciones"
    numero_actual = models.IntegerField(default=0) # El número que se muestra en pantalla
    ultimo_numero_emitido = models.IntegerField(default=0) # Para dar nuevas fichas

    def __str__(self):
        return f"{self.nombre} - Turno: {self.numero_actual}"