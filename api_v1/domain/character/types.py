# Built-in packages

# Third-party packages
from graphene import Interface, ID, String, List

# Local packages
from api_v1.domain.episode.types import Episode


class Character(Interface):
    """A Charater is an individual character within the Star Wars universe."""

    id = ID()
    name = String()
    appears_in = List(Episode)