# Built-in packages

# Third-party packages
from graphql_relay import from_global_id

# Local packages
from api_v1.domain.person import models, types, serializers


def create_person(data: types.PersonCreateInput) -> models.Person:
    serializer = serializers.PersonSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return serializer.instance


def get_person(where: types.PersonWhereUniqueInput) -> models.Person:
    _, person_id = from_global_id(where.get())
    person = models.Person.objects.get(id=person_id)

    return person


def update_person(
    where: types.PersonWhereUniqueInput, data: types.PersonUpdateInput
) -> models.Person:
    person = get_person(where)
    serializer = serializers.PersonSerializer(person, data=data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return serializer.instance


def delete_person(where: types.PersonWhereUniqueInput) -> models.Person:
    person = get_person(where)
    person.delete()

    return person
