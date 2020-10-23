# Built-in packages

# Third-party packages
from graphene import ObjectType

# Local packages
from .domain.starship.schema import StarshipQuery, StarshipMutation
from .domain.person.schema import PersonQuery, PersonMutation
from .domain.planet.schema import PlanetQuery, PlanetMutation
from .domain.episode.schema import EpisodeQuery, EpisodeMutation
from .domain.human.schema import HumanQuery, HumanMutation
from .domain.droid.schema import DroidQuery, DroidMutation


class Query(
    StarshipQuery,
    PersonQuery,
    PlanetQuery,
    EpisodeQuery,
    HumanQuery,
    DroidQuery,
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
    ObjectType,
):
    pass
