from django.contrib import admin
from .models import Cola

@admin.register(Cola)
class ColaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'numero_actual', 'ultimo_numero_emitido')
    search_fields = ('nombre',)