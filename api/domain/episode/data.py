# Built-in packages

# Third-party packages
from graphql_relay import from_global_id

# Local packages
from api.domain.episode import models, types


def create_episode(data: types.EpisodeCreateInput) -> models.Episode:
    created_episode = models.Episode(**data).create()
    return created_episode


def get_episode(where: types.EpisodeWhereUniqueInput) -> models.Episode:
    _, episode_id = from_global_id(where.get())
    episode = models.Episode.objects.get(id=episode_id)
    return episode


def update_episode(
    where: types.EpisodeWhereUniqueInput, data: types.EpisodeUpdateInput
) -> models.Episode:
    updated_episode = get_episode(where).update(**data)
    return updated_episode


def delete_episode(where: types.EpisodeWhereUniqueInput) -> models.Episode:
    deleted_episode = get_episode(where).destroy()
    return deleted_episode
