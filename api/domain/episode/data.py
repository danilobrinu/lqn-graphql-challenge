# Built-in packages
from typing import Union

# Third-party packages
from graphql_relay import from_global_id

# Local packages
from . import models
from . import types


def create_episode(data: types.EpisodeCreateInput) -> models.Episode:
    episode = models.Episode(**data)
    episode.save()
    return episode


def get_episode(where: types.EpisodeWhereUniqueInput) -> Union[models.Episode, None]:
    _, episode_id = from_global_id(where.get())
    episode = models.Episode.objects.get(id=episode_id)
    return episode


def update_episode(
    where: types.EpisodeWhereUniqueInput, data: types.EpisodeUpdateInput
) -> models.Episode:
    episode = get_episode(where)
    episode.save(**data)
    return episode


def delete_episode(where: types.EpisodeWhereUniqueInput) -> models.Episode:
    episode = get_episode(where)
    episode.delete()
    return episode
