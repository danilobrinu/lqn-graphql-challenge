# Built-in packages
from typing import Union

# Third-party packages
from graphql_relay import from_global_id

# Local packages
from . import models
from . import types


def create_human(data: types.HumanCreateInput) -> models.Human:
    human = models.Human(**data)
    human.save()
    return human


def get_human(where: types.HumanWhereUniqueInput) -> models.Human:
    _, human_id = from_global_id(where.get())
    human = models.Human.objects.get(id=human_id)
    return human


def update_human(
    where: types.HumanWhereUniqueInput, data: types.HumanUpdateInput
) -> models.Human:
    human = get_human(where)
    human.update(**data)
    return human


def delete_human(where: types.HumanWhereUniqueInput) -> models.Human:
    human = get_human(where)
    human.delete()
    return human
