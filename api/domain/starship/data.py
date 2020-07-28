# Built-in packages
from typing import Union

# Third-party packages
from graphql_relay import from_global_id

# Local packages
from . import models
from . import types


def create_starship(data: types.StarshipCreateInput) -> models.Starship:
    starship = models.Starship(**data)
    starship.save()
    return starship


def get_starship(where: types.StarshipWhereUniqueInput) -> Union[models.Starship, None]:
    _, starship_id = from_global_id(where.get())
    starship = models.Starship.objects.get(id=starship_id)
    return starship


def update_starship(
    where: types.StarshipWhereUniqueInput, data: types.StarshipUpdateInput
) -> models.Starship:
    starship = get_starship(where)
    starship.save(**data)
    return starship


def delete_starship(where: types.StarshipWhereUniqueInput) -> models.Starship:
    starship = get_starship(where)
    starship.delete()
    return starship
