# Built-in packages

# Third-party packages
import graphql_relay as relay_gql

# Local packages
from api_v1.domain.starship import models, types, serializers, filters


def get_starship(where: types.StarshipWhereUniqueInput) -> models.Starship:
    _, starship_id = relay_gql.from_global_id(where.get("id"))
    starship = models.Starship.objects.get(id=starship_id)
    return starship


def get_starships(where: types.StarshipWhereInput) -> list[models.Starship]:
    return filters.StarshipFilter(where).qs


def create_starship(data: types.StarshipCreateInput) -> models.Starship:
    serializer = serializers.StarshipSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return serializer.instance


def update_starship(
    where: types.StarshipWhereUniqueInput, data: types.StarshipUpdateInput
) -> models.Starship:
    starship = get_starship(where)
    serializer = serializers.StarshipSerializer(starship, data=data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return serializer.instance


def delete_starship(where: types.StarshipWhereUniqueInput) -> models.Starship:
    starship = get_starship(where)
    starship.delete()

    return starship
