# Built-in packages

# Third-party packages
from graphene import Node, ID, String, Float
from graphene import ObjectType, InputObjectType
from graphene_django import DjangoObjectType

# Local packages
from api.utils import create_open_crud_filter_connection
from . import models
from . import filters


class Droid(DjangoObjectType):
    class Meta:
        model = models.Droid
        filter_fields = []
        interfaces = (Node,)


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


class DroidCreateInput(InputObjectType):
    name = String(required=True)


class DroidUpdateInput(InputObjectType):
    name = String()


DroidFilterConnection = create_open_crud_filter_connection(
    "DroidFilterConnection", filters.DroidFilter
)
