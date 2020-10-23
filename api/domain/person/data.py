# Built-in packages

# Third-party packages
from graphql_relay import from_global_id

# Local packages
from api.domain.person import models, types


def create_person(data: types.PersonCreateInput) -> models.Person:
    created_person = models.Person(**data).create()
    return created_person


def get_person(where: types.PersonWhereUniqueInput) -> models.Person:
    _, person_id = from_global_id(where.get())
    person = models.Person.objects.get(id=person_id)
    return person


def update_person(
    where: types.PersonWhereUniqueInput, data: types.PersonUpdateInput
) -> models.Person:
    updated_person = get_person(where).update(**data)
    return updated_person


def delete_person(where: types.PersonWhereUniqueInput) -> models.Person:
    deleted_person = get_person(where).destroy()
    return deleted_person
