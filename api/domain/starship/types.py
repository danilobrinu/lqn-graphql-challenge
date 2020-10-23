# Built-in packages

# Third-party packages
from graphene import Node, ID, String, Float, ObjectType, InputObjectType
from graphene_django import DjangoObjectType

# Local packages
from api.utils.graphene import create_open_crud_filter_connection_field
from api.domain.starship import models, filters


class Starship(DjangoObjectType):
    """A Starship is a single transport craft that has hyperdrive capability."""

    class Meta:
        model = models.Starship
        filter_fields = []
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
    name_in = String()
    name_not_in = String()


class StarshipCreateInput(InputObjectType):
    name = String(required=True)
    length = Float(required=True)


class StarshipUpdateInput(InputObjectType):
    name = String()
    length = Float()


StarshipFilterConnectionField = create_open_crud_filter_connection_field(
    "StarshipFilterConnection", filters.StarshipFilter
)
