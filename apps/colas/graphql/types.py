
import strawberry
from apps.colas.models import Cola

# @strawberry.django.type(Cola)
@strawberry.type
class ColaType:
    id: strawberry.ID
    nombre: str
    numero_actual: int
    ultimo_numero_emitido: int