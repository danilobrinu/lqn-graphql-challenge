# Built-in packages

# Third-party packages
from graphene import Node, ID, String, Float
from graphene import ObjectType, InputObjectType, List, NonNull
from graphene_django import DjangoObjectType

# Local packages
from api.utils import create_open_crud_filter_connection
from . import models
from . import filters


class Planet(DjangoObjectType):
    class Meta:
        model = models.Planet
        filter_fields = []
        interfaces = (Node,)


class PlanetOutputMutation(ObjectType):
    Output = Planet


class PlanetWhereUniqueInput(InputObjectType):
    id = ID()


class PlanetWhereInput(InputObjectType):
    name = String()
    name_not = String()
    name_contains = String()
    name_not_contains = String()
    name_starts_with = String()
    name_not_starts_with = String()
    name_ends_with = String()
    name_in = String()
    name_not_in = String()


class PlanetCreateInput(InputObjectType):
    name = String(required=True)


class PlanetUpdateInput(InputObjectType):
    name = String()


class PlanetManyInput(InputObjectType):
    connect = List(NonNull(PlanetWhereUniqueInput, required=True))


PlanetFilterConnection = create_open_crud_filter_connection(
    "PlanetFilterConnection", filters.PlanetFilter
)
