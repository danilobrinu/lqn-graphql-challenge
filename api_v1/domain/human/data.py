# Built-in packages

# Third-party packages
from graphql_relay import from_global_id

# Local packages
from api_v1.domain.human import models, types, serializers


def create_human(data: types.HumanCreateInput) -> models.Human:
    serializer = serializers.HumanSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return serializer.instance


def get_human(where: types.HumanWhereUniqueInput) -> models.Human:
    _, human_id = from_global_id(where.get())
    human = models.Human.objects.get(id=human_id)

    return human


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
