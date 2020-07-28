# Built-in packages
from typing import Union

# Third-party packages
from graphql_relay import from_global_id

# Local packages
from . import models
from . import types


def create_person(data: types.PersonCreateInput) -> models.Person:
    person = models.Person(**data)
    person.save()
    return person


def get_person(where: types.PersonWhereUniqueInput) -> Union[models.Person, None]:
    _, person_id = from_global_id(where.get())
    person = models.Person.objects.get(id=person_id)
    return person


def update_person(
    where: types.PersonWhereUniqueInput, data: types.PersonUpdateInput
) -> models.Person:
    person = get_person(where)
    person.save(**data)
    return person


def delete_person(where: types.PersonWhereUniqueInput) -> models.Person:
    person = get_person(where)
    person.delete()
    return person
