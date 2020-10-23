# Built-in packages

# Third-party packages
from graphene import Node, ID, String, ObjectType, InputObjectType  # skipcq: PYL-W0611
from graphene_django import DjangoObjectType

# Local packages
from api.utils.graphene import create_open_crud_filter_connection_field
from api.domain.character.types import Character  # skipcq: PYL-W0611
from api.domain.droid import models, filters


class Droid(DjangoObjectType, interfaces=(Character, Node,)):
    """An object with an ID."""

    class Meta:
        model = models.Droid
        filter_fields = []


class DroidOutputMutation(ObjectType):
    Output = Droid


class DroidWhereUniqueInput(InputObjectType):
    id = ID()


class DroidWhereInput(InputObjectType):
    name = String()
    name_not = String()
    name_contains = String()
    name_not_contains = String()
    name_starts_with = String()
    name_not_starts_with = String()
    name_ends_with = String()
    name_in = String()
    name_not_in = String()
    primary_function = String()
    primary_function_not = String()
    primary_function_contains = String()
    primary_function_not_contains = String()
    primary_function_starts_with = String()
    primary_function_not_starts_with = String()
    primary_function_ends_with = String()
    primary_function_in = String()
    primary_function_not_in = String()


class DroidCreateInput(InputObjectType):
    name = String(required=True)
    primary_function = String(required=True)


class DroidUpdateInput(InputObjectType):
    name = String()
    primary_function = String()


DroidFilterConnectionField = create_open_crud_filter_connection_field(
    "DroidFilterConnection", filters.DroidFilter
)
