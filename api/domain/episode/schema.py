# Built-in package

# Third-party packages
from django.db.transaction import atomic
from graphene import ObjectType, Mutation, ResolveInfo
from graphene.relay import Node

# Local packages
from api.domain.episode import models, types
from api.domain.episode.data import create_episode, update_episode, delete_episode


class CreateEpisode(types.EpisodeOutputMutation, Mutation):
    class Arguments:
        data = types.EpisodeCreateInput(required=True)

    @atomic
    def mutate(
        _root: models.Episode, _info: ResolveInfo, data: types.EpisodeCreateInput
    ) -> models.Episode:
        return create_episode(data)


class UpdateEpisode(types.EpisodeOutputMutation, Mutation):
    class Arguments:
        data = types.EpisodeUpdateInput(required=True)
        where = types.EpisodeWhereUniqueInput(required=True)

    @atomic
    def mutate(
        _root: models.Episode,
        info: ResolveInfo,
        where: types.EpisodeWhereUniqueInput,
        data: types.EpisodeUpdateInput,
    ) -> models.Episode:
        return update_episode(where, data)


class DeleteEpisode(types.EpisodeOutputMutation, Mutation):
    class Arguments:
        where = types.EpisodeWhereUniqueInput(required=True)

    @atomic
    def mutate(
        _root: models.Episode, info: ResolveInfo, where: types.EpisodeWhereUniqueInput
    ) -> models.Episode:
        return delete_episode(where)


class EpisodeQuery(ObjectType):
    episode = Node.Field(types.Episode)
    episodes = types.EpisodeFilterConnectionField(
        types.Episode, where=types.EpisodeWhereInput()
    )


class EpisodeMutation(ObjectType):
    create_episode = CreateEpisode.Field(required=True)
    update_episode = UpdateEpisode.Field()
    delete_episode = DeleteEpisode.Field()
