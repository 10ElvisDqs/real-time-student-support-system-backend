import strawberry
from asgiref.sync import sync_to_async
from django.db import transaction
from channels.layers import get_channel_layer
from apps.colas.models import Cola
from .types import ColaType

# 1. Función auxiliar para la BD (Síncrona)
@sync_to_async
def avanzar_turno_db(cola_id):
    with transaction.atomic():
        cola = Cola.objects.select_for_update().get(pk=cola_id)
        cola.numero_actual += 1
        cola.save()
        return cola

# 2. La clase Mutation (ESTO ES LO QUE TE FALTABA O ESTABA MAL NOMBRADO)
@strawberry.type
class Mutation:
    @strawberry.mutation
    async def llamar_siguiente(self, cola_id: strawberry.ID) -> ColaType:
        # 1. Obtenemos el objeto de la BD
        cola = await avanzar_turno_db(cola_id)

        # 2. Redis / Channels
        channel_layer = get_channel_layer()
        
        # --- AQUÍ ESTÁ EL CAMBIO ---
        # No podemos enviar 'cola' (objeto). Enviamos un diccionario.
        cola_data = {
            "id": cola.id,
            "nombre": cola.nombre,
            "numero_actual": cola.numero_actual,
            "ultimo_numero_emitido": cola.ultimo_numero_emitido
        }

        await channel_layer.group_send(
            f"cola_{cola_id}",
            {
                "type": "update_cola", 
                "data": cola_data  # <--- Enviamos el diccionario, no el objeto
            }
        )

        return cola