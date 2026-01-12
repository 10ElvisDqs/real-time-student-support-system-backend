import strawberry
from apps.colas.graphql.mutations import Mutation as ColasMutation
from apps.colas.graphql.subscriptions import Subscription as ColasSubscription

# Query básica para obtener el estado inicial (cuando el estudiante abre la app)
from apps.colas.models import Cola
from apps.colas.graphql.types import ColaType

@strawberry.type
class Query:
    @strawberry.field
    def obtener_cola(self, cola_id: strawberry.ID) -> ColaType:
        return Cola.objects.get(pk=cola_id)

class Mutation(ColasMutation):
    pass

class Subscription(ColasSubscription):
    pass

schema = strawberry.Schema(query=Query, mutation=Mutation, subscription=Subscription)