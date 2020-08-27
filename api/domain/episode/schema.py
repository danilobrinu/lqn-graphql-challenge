# Built-in package

# Third-party packages
from django.db.transaction import atomic
from graphene import ObjectType, Mutation
from graphene.relay import Node

# Local packages
from api.utils import create_open_crud_filter_connection
from . import models
from . import types
from . import filters

from .data import get_episode, create_episode, update_episode, delete_episode


class CreateEpisode(types.EpisodeOutputMutation, Mutation):
    class Arguments:
        data = types.EpisodeCreateInput(required=True)

    @atomic
    def mutate(self, info, data: types.EpisodeCreateInput):
        return create_episode(data)


class UpdateEpisode(types.EpisodeOutputMutation, Mutation):
    class Arguments:
        data = types.EpisodeUpdateInput(required=True)
        where = types.EpisodeWhereUniqueInput(required=True)

    @atomic
    def mutate(
        self,
        info,
        where: types.EpisodeWhereUniqueInput,
        data: types.EpisodeUpdateInput,
    ):
        return update_episode(where, data)


class DeleteEpisode(types.EpisodeOutputMutation, Mutation):
    class Arguments:
        where = types.EpisodeWhereUniqueInput(required=True)

    @atomic
    def mutate(self, info, where: types.EpisodeWhereUniqueInput):
        return delete_episode(where)


class EpisodeQuery(ObjectType):
    episode = Node.Field(types.Episode)
    episodes = types.EpisodeFilterConnection(
        types.Episode, where=types.EpisodeWhereInput()
    )


class EpisodeMutation(ObjectType):
    create_episode = CreateEpisode.Field(required=True)
    update_episode = UpdateEpisode.Field()
    delete_episode = DeleteEpisode.Field()
