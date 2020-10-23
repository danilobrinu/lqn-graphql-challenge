# Built-in packages
from decimal import Decimal

# Third-party packages
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from graphql_relay import to_global_id
from pytest import mark, raises, fixture

# Local packages
from api.domain.starship.models import Starship
from api.domain.starship.data import (
    create_starship,
    get_starship,
    update_starship,
    delete_starship,
)
from .utils import create_random_starship


@fixture
def starship_one():
    return create_random_starship()


@fixture
def starship_two():
    return create_random_starship()


@fixture
def starship_three():
    return create_random_starship()


@mark.django_db
@mark.parametrize(
    "valid_case",
    [
        ({"name": "Starship 1", "length": 12}, "Starship 1"),
        ({"name": "Starship 2", "length": 12.65}, "Starship 2"),
        ({"name": "Starship 3", "length": Decimal(12.65)}, "Starship 3"),
        ({"name": "Starship 3", "length": "12.65"}, "Starship 3"),
    ],
)
def test_create_starship_valid_cases(valid_case):
    data, expected_output = valid_case
    starship = create_starship(data)
    starship_exist = starship is not None
    starship_name = starship.name

    assert starship_exist
    assert starship_name == expected_output


@mark.django_db
@mark.parametrize(
    "invalid_case",
    [
        ({}, IntegrityError),
        ({"name": None, "length": None}, IntegrityError),
        ({"name": "Starship 1", "length": None}, IntegrityError),
        ({"name": None, "length": 15.65}, IntegrityError),
    ],
)
def test_create_starship_invalid_cases(invalid_case):
    data, expected_error = invalid_case

    with raises(expected_error):
        create_starship(data)


@mark.django_db
def test_get_starship(starship_one):
    where = {"id": to_global_id(Starship.__name__, starship_one.id)}
    starship = get_starship(where)
    starship_id = starship.id
    starship_one_id = starship_one.id

    assert starship is not None
    assert starship_id == starship_one_id


@mark.django_db
def test_get_starship_does_not_exist():
    where = {"id": to_global_id(Starship.__name__, "0")}

    with raises(ObjectDoesNotExist):
        get_starship(where)


@mark.django_db
def test_update_starship(starship_two):
    where = {"id": to_global_id(Starship.__name__, starship_two.id)}
    data = {"name": "Starship Updated"}
    expected_output = data.name
    starship = update_starship(where, data)
    starship_exist = starship is not None
    starship_name = expected_output

    assert starship_exist
    assert starship_name == expected_output


@mark.django_db
def test_delete_starship(starship_three):
    where = {"id": to_global_id(Starship.__name__, starship_three.id)}
    delete_starship(where)

    with raises(ObjectDoesNotExist):
        get_starship(where)
