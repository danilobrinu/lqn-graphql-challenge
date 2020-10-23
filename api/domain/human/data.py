# Built-in packages

# Third-party packages
from graphql_relay import from_global_id

# Local packages
from api.domain.human import models, types


def create_human(data: types.HumanCreateInput) -> models.Human:
    created_human = models.Human(**data).create()
    return created_human


def get_human(where: types.HumanWhereUniqueInput) -> models.Human:
    _, human_id = from_global_id(where.get())
    human = models.Human.objects.get(id=human_id)
    return human


def update_human(
    where: types.HumanWhereUniqueInput, data: types.HumanUpdateInput
) -> models.Human:
    updated_human = get_human(where).update(**data)
    return updated_human


def delete_human(where: types.HumanWhereUniqueInput) -> models.Human:
    deleted_human = get_human(where).destroy()
    return deleted_human
