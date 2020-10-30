# Built-in packages

# Third-party packages
import graphql_relay as relay_gql

# Local packages
from api_v1.domain.episode import models, types, serializers, filters


def get_episode(where: types.EpisodeWhereUniqueInput) -> models.Episode:
    _, episode_id = relay_gql.from_global_id(where.get())
    episode = models.Episode.objects.get(id=episode_id)

    return episode


def get_episodes(where: types.EpisodeWhereInput) -> list[models.Episode]:
    return filters.EpisodeFilter(where).qs


def create_episode(data: types.EpisodeCreateInput) -> models.Episode:
    serializer = serializers.EpisodeSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return serializer.instance


def update_episode(
    where: types.EpisodeWhereUniqueInput, data: types.EpisodeUpdateInput
) -> models.Episode:
    episode = get_episode(where)
    serializer = serializers.EpisodeSerializer(episode, data=data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return serializer.instance


def delete_episode(where: types.EpisodeWhereUniqueInput) -> models.Episode:
    episode = get_episode(where)
    episode.delete()

    return episode
