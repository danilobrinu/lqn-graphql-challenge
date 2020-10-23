# Built-in packages

# Third-party packages
from graphql_relay import from_global_id

# Local packages
from api.domain.starship import models, types


def create_starship(data: types.StarshipCreateInput) -> models.Starship:
    created_starship = models.Starship(**data).create()
    return created_starship


def get_starship(where: types.StarshipWhereUniqueInput) -> models.Starship:
    _, starship_id = from_global_id(where.get("id"))
    starship = models.Starship.objects.get(id=starship_id)
    return starship


def update_starship(
    where: types.StarshipWhereUniqueInput, data: types.StarshipUpdateInput
) -> models.Starship:
    updated_starship = get_starship(where).update(**data)
    return updated_starship


def delete_starship(where: types.StarshipWhereUniqueInput) -> models.Starship:
    deleted_starship = get_starship(where).destroy()
    return deleted_starship
