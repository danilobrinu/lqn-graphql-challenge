# Built-in packages

# Third-party packages
import graphql_relay as relay_gql

# Local packages
from api_v1.domain.droid import models, types, serializers, filters


def get_droid(where: types.DroidWhereUniqueInput) -> models.Droid:
    _, droid_id = relay_gql.from_global_id(where.get("id"))
    droid = models.Droid.objects.get(id=droid_id)

    return droid


def get_droids(where: types.DroidWhereInput) -> list[models.Droid]:
    return filters.DroidFilter(where).qs


def create_droid(data: types.DroidCreateInput) -> models.Droid:
    serializer = serializers.DroidSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return serializer.instance


def update_droid(
    where: types.DroidWhereUniqueInput, data: types.DroidUpdateInput
) -> models.Droid:
    droid = get_droid(where)
    serializer = serializers.DroidSerializer(droid, data=data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return serializer.instance


def delete_droid(where: types.DroidWhereUniqueInput) -> models.Droid:
    droid = get_droid(where)
    droid.delete()

    return droid
