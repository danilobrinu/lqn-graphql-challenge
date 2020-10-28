# Built-in packages

# Third-party packages
from graphene import (
    Node,
    Field,
    ID,
    String,
    Float,
    Decimal,
    List,
    ObjectType,
    InputObjectType,
)
from graphene.relay.node import NodeField
from graphene_django import DjangoObjectType

# Local packages
from api_v1.utils.graphene import (
    create_open_crud_filter_connection_field,
    create_open_crud_filter_field,
)
from api_v1.domain.starship import models, filters


class Starship(DjangoObjectType):
    """A Starship is a single transport craft that has hyperdrive capability."""

    class Meta:
        model = models.Starship
        filter_fields = ("name", "length")
        interfaces = (Node,)


class StarshipOutputMutation(ObjectType):
    Output = Starship


class StarshipWhereUniqueInput(InputObjectType):
    id = ID()


class StarshipWhereInput(InputObjectType):
    name = String()
    name_not = String()
    name_contains = String()
    name_not_contains = String()
    name_starts_with = String()
    name_not_starts_with = String()
    name_ends_with = String()
    name_not_ends_with = String()
    name_in = List(String)
    name_not_in = List(String)
    length = Decimal()
    length_not = Decimal()
    length_lt = Decimal()
    length_lte = Decimal()
    length_gt = Decimal()
    length_gte = Decimal()
    length_in = List(Decimal)
    length_not_in = List(Decimal)


class StarshipCreateInput(InputObjectType):
    name = String(required=True)
    length = Float(required=True)


class StarshipUpdateInput(InputObjectType):
    name = String()
    length = Float()


StarshipFilterConnectionField = create_open_crud_filter_connection_field(
    "StarshipFilterConnection", filters.StarshipFilter
)

