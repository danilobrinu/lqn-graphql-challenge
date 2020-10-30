# Built-in packages

# Third-party packages
import graphql_relay as relay_gql

# Local packages
from api_v1.domain.human import models, types, serializers, filters


def get_human(where: types.HumanWhereUniqueInput) -> models.Human:
    _, human_id = relay_gql.from_global_id(where.get())
    human = models.Human.objects.get(id=human_id)

    return human


def get_humans(where: types.HumanWhereInput) -> list[models.Human]:
    return filters.HumanFilter(where).qs


def create_human(data: types.HumanCreateInput) -> models.Human:
    serializer = serializers.HumanSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return serializer.instance


def update_human(
    where: types.HumanWhereUniqueInput, data: types.HumanUpdateInput
) -> models.Human:
    human = get_human(where)
    serializer = serializers.HumanSerializer(human, data=data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return serializer.instance


def delete_human(where: types.HumanWhereUniqueInput) -> models.Human:
    human = get_human(where)
    human.delete()

    return human
