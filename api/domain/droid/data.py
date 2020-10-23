# Built-in packages
from typing import Union

# Third-party packages
from graphql_relay import from_global_id

# Local packages
from api.domain.droid import models, types


def create_droid(data: types.DroidCreateInput) -> models.Droid:
    created_droid = models.Droid(**data).create()
    return created_droid


def get_droid(where: types.DroidWhereUniqueInput) -> models.Droid:
    _, droid_id = from_global_id(where.get("id"))
    droid = models.Droid.objects.get(id=droid_id)
    return droid


def update_droid(
    where: types.DroidWhereUniqueInput, data: types.DroidUpdateInput
) -> models.Droid:
    updated_droid = get_droid(where).update(**data)
    return updated_droid


def delete_droid(where: types.DroidWhereUniqueInput) -> models.Droid:
    deleted_droid = get_droid(where).destroy()
    return deleted_droid
