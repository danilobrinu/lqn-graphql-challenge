# Built-in packages
from typing import Union

# Third-party packages
from graphql_relay import from_global_id

# Local packages
from . import models
from . import types


def create_droid(data: types.DroidCreateInput) -> models.Droid:
    droid = models.Droid(**data)
    droid.save()
    return droid


def get_droid(where: types.DroidWhereUniqueInput) -> models.Droid:
    _, droid_id = from_global_id(where.get("id"))
    droid = models.Droid.objects.get(id=droid_id)
    return droid


def update_droid(
    where: types.DroidWhereUniqueInput, data: types.DroidUpdateInput
) -> models.Droid:
    droid = get_droid(where)
    droid.update(**data)
    return droid


def delete_droid(where: types.DroidWhereUniqueInput) -> models.Droid:
    droid = get_droid(where)
    droid.delete()
    return droid
