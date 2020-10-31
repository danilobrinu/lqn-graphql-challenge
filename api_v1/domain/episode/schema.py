# Built-in package

# Third-party packages
import graphene as gql
from django.db.transaction import atomic

# Local packages
from . import models, types, crud


class CreateEpisode(types.EpisodeOutputMutation, gql.Mutation):
    class Arguments:
        data = types.EpisodeCreateInput(required=True)

    @atomic
    # skipcq: PYL-E0213, PYL-R0201
    def mutate(
        _root: models.Episode, _info: gql.ResolveInfo, data: types.EpisodeCreateInput
    ) -> models.Episode:
        return crud.create_episode(data)


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
        return crud.update_episode(where, data)


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
        return crud.delete_episode(where)


class Query(gql.ObjectType):
    episode = gql.Field(
        types.Episode, where=types.EpisodeWhereUniqueInput(required=True)
    )
    episodes = gql.Field(
        gql.List(gql.NonNull(types.Episode)), where=types.EpisodeWhereInput()
    )

    # skipcq: PYL-E0213, PYL-R0201
    def resolve_episode(
        _root: models.Episode,
        _info: gql.ResolveInfo,
        where: types.EpisodeWhereUniqueInput,
    ) -> models.Episode:
        return crud.get_episode(where)

    # skipcq: PYL-E0213, PYL-R0201
    def resolve_episodes(
        _root: models.Episode, _info: gql.ResolveInfo, where: types.EpisodeWhereInput
    ) -> list[models.Episode]:
        return crud.get_episodes(where)


class Mutation(gql.ObjectType):
    create_episode = CreateEpisode.Field(required=True)
    update_episode = UpdateEpisode.Field()
    delete_episode = DeleteEpisode.Field()
