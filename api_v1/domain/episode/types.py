# Built-in packages

# Third-party packages
import graphene as gql
from graphene_django import DjangoObjectType

# Local packages
from api_v1.utils.graphene import create_open_crud_filter_connection_field
from api_v1.domain.episode import models, filters
from api_v1.domain.person.types import PersonOneInput
from api_v1.domain.planet.types import PlanetManyInput


class Episode(DjangoObjectType):
    """A Episode is a single film."""

    class Meta:
        model = models.Episode
        filter_fields = []
        interfaces = (gql.Node,)


class EpisodeOutputMutation(gql.ObjectType):
    Output = Episode


class EpisodeWhereUniqueInput(gql.InputObjectType):
    id = gql.ID()


class EpisodeWhereInput(gql.InputObjectType):
    title = gql.String()
    title_not = gql.String()
    title_contains = gql.String()
    title_not_contains = gql.String()
    title_starts_with = gql.String()
    title_not_starts_with = gql.String()
    title_ends_with = gql.String()
    title_in = gql.String()
    title_not_in = gql.String()


class EpisodeCreateInput(gql.InputObjectType):
    title = gql.String(required=True)
    opening_text = gql.String(required=True)
    release_date = gql.Date(required=True)
    director = PersonOneInput(required=True)
    producers = PlanetManyInput(required=True)


class EpisodeUpdateInput(gql.InputObjectType):
    title = gql.String()
    opening_text = gql.String()
    release_date = gql.Date()
    director = PersonOneInput()
    producers = PlanetManyInput()


class EpisodeManyInput(gql.InputObjectType):
    connect = gql.List(gql.NonNull(EpisodeWhereUniqueInput, required=True))


EpisodeFilterConnectionField = create_open_crud_filter_connection_field(
    "EpisodeFilterConnection", filters.EpisodeFilter
)
