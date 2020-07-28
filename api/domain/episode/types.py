# Built-in packages

# Third-party packages
from graphene import Node, ID, String, Float, Date, Field, List, NonNull
from graphene import ObjectType, InputObjectType
from graphene_django import DjangoObjectType

# Local packages
from api.utils import create_open_crud_filter_connection
from . import models
from . import filters
from ..person.types import PersonOneInput
from ..planet.types import PlanetManyInput


class Episode(DjangoObjectType):
    class Meta:
        model = models.Episode
        filter_fields = []
        interfaces = (Node,)


class EpisodeOutputMutation(ObjectType):
    Output = Episode


class EpisodeWhereUniqueInput(InputObjectType):
    id = ID()


class EpisodeWhereInput(InputObjectType):
    title = String()
    title_not = String()
    title_contains = String()
    title_not_contains = String()
    title_starts_with = String()
    title_not_starts_with = String()
    title_ends_with = String()
    title_in = String()
    title_not_in = String()


class EpisodeCreateInput(InputObjectType):
    title = String(required=True)
    opening_text = String(required=True)
    release_date = Date(required=True)
    director = PersonOneInput(required=True)
    producers = PlanetManyInput(required=True)


class EpisodeUpdateInput(InputObjectType):
    title = String()
    opening_text = String()
    release_date = Date()
    director = PersonOneInput()
    producers = PlanetManyInput()


class EpisodeManyInput(InputObjectType):
    connect = List(NonNull(EpisodeWhereUniqueInput, required=True))


EpisodeFilterConnection = create_open_crud_filter_connection(
    "EpisodeFilterConnection", filters.EpisodeFilter
)
