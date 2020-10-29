# Built-in package

# Third-party packages
import graphene as gql
from django.db.transaction import atomic

# Local packages
from api_v1.domain.episode import models, types
from api_v1.domain.episode.data import (
    get_episode,
    create_episode,
    update_episode,
    delete_episode,
)


class CreateEpisode(types.EpisodeOutputMutation, gql.Mutation):
    class Arguments:
        data = types.EpisodeCreateInput(required=True)

    @atomic
    # skipcq: PYL-E0213, PYL-R0201
    def mutate(
        _root: models.Episode, _info: gql.ResolveInfo, data: types.EpisodeCreateInput
    ) -> models.Episode:
        return create_episode(data)


class UpdateEpisode(types.EpisodeOutputMutation, gql.Mutation):
    class Arguments:
        data = types.EpisodeUpdateInput(required=True)
        where = types.EpisodeWhereUniqueInput(required=True)

    @atomic
    # skipcq: PYL-E0213, PYL-R0201
    def mutate(
        _root: models.Episode,
        info: gql.ResolveInfo,
        where: types.EpisodeWhereUniqueInput,
        data: types.EpisodeUpdateInput,
    ) -> models.Episode:
        return update_episode(where, data)


class DeleteEpisode(types.EpisodeOutputMutation, gql.Mutation):
    class Arguments:
        where = types.EpisodeWhereUniqueInput(required=True)

    @atomic
    # skipcq: PYL-E0213, PYL-R0201
    def mutate(
        _root: models.Episode,
        info: gql.ResolveInfo,
        where: types.EpisodeWhereUniqueInput,
    ) -> models.Episode:
        return delete_episode(where)


class Query(gql.ObjectType):
    episode = gql.Field(
        types.Episode, where=types.EpisodeWhereUniqueInput(required=True)
    )
    episodes = types.EpisodeFilterConnectionField(
        types.Episode, where=types.EpisodeWhereInput()
    )

    def resolve_episode(
        _root: models.Episode,
        _info: gql.ResolveInfo,
        where: types.EpisodeWhereUniqueInput,
    ):
        return get_episode(where)


class Mutation(gql.ObjectType):
    create_episode = CreateEpisode.Field(required=True)
    update_episode = UpdateEpisode.Field()
    delete_episode = DeleteEpisode.Field()
