# Built-in packages

# Third-party packages
from graphene import Node, ID, String, List, NonNull
from graphene import ObjectType, InputObjectType
from graphene_django import DjangoObjectType

# Local packages
from api.utils.graphene import create_open_crud_filter_connection_field
from api.domain.character.types import Character
from api.domain.human import models, filters


class Human(DjangoObjectType, interfaces=(Character, Node,)):
    """A Human is an character within the Star Wars universe."""

    class Meta:
        model = models.Human
        filter_fields = []


class HumanOutputMutation(ObjectType):
    Output = Human


class HumanWhereUniqueInput(InputObjectType):
    id = ID()


class HumanWhereInput(InputObjectType):
    name = String()
    name_not = String()
    name_contains = String()
    name_not_contains = String()
    name_starts_with = String()
    name_not_starts_with = String()
    name_ends_with = String()
    name_in = String()
    name_not_in = String()


class HumanManyInput(InputObjectType):
    connect = List(NonNull(HumanWhereUniqueInput, required=True))


class HumanCreateInput(InputObjectType):
    name = String(required=True)
    home_planet = String(required=True)
    friends = HumanManyInput()


class HumanUpdateInput(InputObjectType):
    name = String()
    human_planet = String()
    friends = HumanManyInput()


HumanFilterConnectionField = create_open_crud_filter_connection_field(
    "HumanFilterConnection", filters.HumanFilter
)
