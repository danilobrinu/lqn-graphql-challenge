# Built-in packages

# Third-party packages
import graphene as gql

# Local packages
from api_v1.domain.episode.types import Episode


class Character(gql.Interface):
    """A Charater is an individual character within the Star Wars universe."""

    id = gql.ID()
    name = gql.String()
    appears_in = gql.List(Episode)
