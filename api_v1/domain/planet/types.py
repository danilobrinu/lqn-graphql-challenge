# Built-in packages

# Third-party packages
import graphene as gql
from graphene_django import DjangoObjectType

# Local packages
from api_v1.utils.graphene import create_open_crud_filter_connection_field
from api_v1.domain.planet import models, filters


class Planet(DjangoObjectType):
    """A Planet is a large mass, planet or planetoid in the Star Wars Universe, at the time of 0 ABY."""

    class Meta:
        model = models.Planet
        filter_fields = []
        interfaces = (gql.Node,)


class PlanetOutputMutation(gql.ObjectType):
    Output = Planet


class PlanetWhereUniqueInput(gql.InputObjectType):
    id = gql.ID()


class PlanetWhereInput(gql.InputObjectType):
    name = gql.String()
    name_not = gql.String()
    name_contains = gql.String()
    name_not_contains = gql.String()
    name_starts_with = gql.String()
    name_not_starts_with = gql.String()
    name_ends_with = gql.String()
    name_in = gql.String()
    name_not_in = gql.String()


class PlanetCreateInput(gql.InputObjectType):
    name = gql.String(required=True)


class PlanetUpdateInput(gql.InputObjectType):
    name = gql.String()


class PlanetManyInput(gql.InputObjectType):
    connect = gql.List(gql.NonNull(PlanetWhereUniqueInput, required=True))


PlanetFilterConnectionField = create_open_crud_filter_connection_field(
    "PlanetFilterConnection", filters.PlanetFilter
)
