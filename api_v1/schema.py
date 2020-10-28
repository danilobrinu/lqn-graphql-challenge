# Built-in packages

# Third-party packages
from graphene import ObjectType, Schema

# Local packages
from .domain.starship.schema import Query as StarshipQuery, Mutation as StarshipMutation
from .domain.person.schema import Query as PersonQuery, Mutation as PersonMutation
from .domain.planet.schema import Query as PlanetQuery, Mutation as PlanetMutation
from .domain.episode.schema import Query as EpisodeQuery, Mutation as EpisodeMutation
from .domain.human.schema import Query as HumanQuery, Mutation as HumanMutation
from .domain.droid.schema import Query as DroidQuery, Mutation as DroidMutation


class Query(
    StarshipQuery,
    PersonQuery,
    PlanetQuery,
    EpisodeQuery,
    HumanQuery,
    DroidQuery,
    # The ObjectType class should be the last one always
    ObjectType,
):
    pass


class Mutation(
    StarshipMutation,
    PersonMutation,
    PlanetMutation,
    EpisodeMutation,
    HumanMutation,
    DroidMutation,
    # The ObjectType class should be the last one always
    ObjectType,
):
    pass


schema = Schema(query=Query, mutation=Mutation)
