# Built-in packages

# Third-party packages
from pytest import mark, raises, fixture

# Local packages
from api_v1.domain.human.models import Human
from api_v1.domain.human.data import create_human, get_human, update_human, delete_human
from .utils import create_random_human


@fixture
def human_one():
    return create_random_human()


@fixture
def human_two():
    return create_random_human()


@fixture
def human_three():
    return create_random_human()


# @mark.django_db
# @mark.parametrize(
#     "valid_case",
#     [
#         (
#             {
#                 "name": "Human 1",
#                 "appears_in": [],
#                 "home_planet": "Earth",
#                 "friends": [],
#             },
#             "Human 1",
#         ),
#     ],
# )
# def test_create_human_valid_cases(valid_case):
#     data, expected_output = valid_case
#     human = create_human(data)

#     assert human is not None
#     assert human.name is expected_output
