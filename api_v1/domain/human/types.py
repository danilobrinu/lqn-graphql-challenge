# Built-in packages

# Third-party packages
import graphene as gql
from graphene_django import DjangoObjectType

# Local packages
from api_v1.utils.graphene import create_open_crud_filter_connection_field
from api_v1.domain.character.types import Character  # skipcq: PYL-W0611
from api_v1.domain.human import models, filters


class Human(DjangoObjectType, interfaces=(Character, gql.Node,)):
    """A Human is an character within the Star Wars universe."""

    class Meta:
        model = models.Human
        filter_fields = []


class HumanOutputMutation(gql.ObjectType):
    Output = Human


class HumanWhereUniqueInput(gql.InputObjectType):
    id = gql.ID()


class HumanWhereInput(gql.InputObjectType):
    name = gql.String()
    name_not = gql.String()
    name_contains = gql.String()
    name_not_contains = gql.String()
    name_starts_with = gql.String()
    name_not_starts_with = gql.String()
    name_ends_with = gql.String()
    name_in = gql.String()
    name_not_in = gql.String()


class HumanManyInput(gql.InputObjectType):
    connect = gql.List(gql.NonNull(HumanWhereUniqueInput, required=True))


class HumanCreateInput(gql.InputObjectType):
    name = gql.String(required=True)
    home_planet = gql.String(required=True)
    friends = HumanManyInput()


class HumanUpdateInput(gql.InputObjectType):
    name = gql.String()
    human_planet = gql.String()
    friends = HumanManyInput()


HumanFilterConnectionField = create_open_crud_filter_connection_field(
    "HumanFilterConnection", filters.HumanFilter
)
