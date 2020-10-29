# Built-in packages

# Third-party packages
import graphene as gql
from graphene.relay.node import NodeField
from graphene_django import DjangoObjectType

# Local packages
from api_v1.utils.graphene import create_open_crud_filter_connection_field
from api_v1.domain.starship import models, filters


class Starship(DjangoObjectType):
    """A Starship is a single transport craft that has hyperdrive capability."""

    class Meta:
        model = models.Starship
        filter_fields = ("name", "length")
        interfaces = (gql.Node,)


class StarshipOutputMutation(gql.ObjectType):
    Output = Starship


class StarshipWhereUniqueInput(gql.InputObjectType):
    id = gql.ID()


class StarshipWhereInput(gql.InputObjectType):
    name = gql.String()
    name_not = gql.String()
    name_contains = gql.String()
    name_not_contains = gql.String()
    name_starts_with = gql.String()
    name_not_starts_with = gql.String()
    name_ends_with = gql.String()
    name_not_ends_with = gql.String()
    name_in = gql.List(gql.String)
    name_not_in = gql.List(gql.String)
    length = gql.Decimal()
    length_not = gql.Decimal()
    length_lt = gql.Decimal()
    length_lte = gql.Decimal()
    length_gt = gql.Decimal()
    length_gte = gql.Decimal()
    length_in = gql.List(gql.Decimal)
    length_not_in = gql.List(gql.Decimal)


class StarshipCreateInput(gql.InputObjectType):
    name = gql.String(required=True)
    length = gql.Float(required=True)


class StarshipUpdateInput(gql.InputObjectType):
    name = gql.String()
    length = gql.Float()


StarshipFilterConnectionField = create_open_crud_filter_connection_field(
    "StarshipFilterConnection", filters.StarshipFilter
)

