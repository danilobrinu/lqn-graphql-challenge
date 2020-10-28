# Built-in packages
from os import path

# Third-party packages
from pytest import fixture, mark
from snapshottest.pytest import SnapshotTest, snapshot
from graphql_relay import to_global_id
from graphene.test import Client as GraphQLClient

# Local packages
from api_v1.schema import schema
from api_v1.domain.starship.data import create_starship
from api_v1.domain.starship.models import Starship
from api_v1.domain.starship.types import (
    StarshipCreateInput,
    StarshipWhereInput,
    StarshipUpdateInput,
)

GRAPHQL_PATH = path.join(path.dirname(__file__), "graphql")


@fixture
def starship_one() -> Starship:
    starship = create_starship({"name": "Starship One", "length": "9.00"})

    return starship


@fixture
def starship_two() -> Starship:
    starship = create_starship({"name": "Starship Two", "length": "10.00"})

    return starship


@fixture
def starship_three() -> Starship:
    starship = create_starship({"name": "Starship Three", "length": "11.00"})

    return starship


@fixture
def graphql_client() -> GraphQLClient:
    client = GraphQLClient(schema)

    return client


@mark.django_db
def test_query_starship(
    graphql_client: GraphQLClient, starship_one: Starship, snapshot: SnapshotTest
):
    with open(path.join(GRAPHQL_PATH, "query_get_starships.graphql")) as file:
        query = file.read()
        starship_global_id = to_global_id(Starship.__name__, starship_one.id)
        variables = {"where": {"id": starship_global_id}}
        response = graphql_client.execute(query, variable_values=variables)
        snapshot.assert_match(response)


@mark.django_db
def test_query_starships(
    graphql_client: GraphQLClient,
    starship_one: Starship,
    starship_two: Starship,
    starship_three: Starship,
    snapshot: SnapshotTest,
):
    with open(path.join(GRAPHQL_PATH, "query_get_starships.graphql")) as file:
        query = file.read()
        response = graphql_client.execute(query)
        snapshot.assert_match(response)


@mark.django_db
@mark.parametrize(
    "where",
    [
        {},
        {"name": "Starship One"},
        {"nameNot": "Starship One"},
        {"nameContains": "Starship"},
        {"nameNotContains": "Two"},
        {"nameStartsWith": "Starship"},
        {"nameNotStartsWith": "Starship"},
        {"nameEndsWith": "One"},
        {"nameNotEndsWith": "One"},
        {"nameIn": ["Starship One"]},
        {"nameNotIn": ["Starship One", "Starship Two"]},
        {"length": "10.00"},
        {"lengthNot": "10.00"},
        {"lengthLt": "10.00"},
        {"lengthLte": "10.00"},
        {"lengthGt": "10.00"},
        {"lengthGte": "10.00"},
        {"lengthIn": ["9", "10"]},
        {"lengthNotIn": ["10", "11"]},
    ],
)
def test_query_starships_with_filters(
    graphql_client: GraphQLClient,
    starship_one: Starship,
    starship_two: Starship,
    starship_three: Starship,
    snapshot: SnapshotTest,
    where: StarshipWhereInput,
):
    with open(
        path.join(GRAPHQL_PATH, "query_get_starships_with_filters.graphql")
    ) as file:
        query = file.read()
        variables = {"where": where}
        response = graphql_client.execute(query, variable_values=variables)
        snapshot.assert_match(response)


@mark.django_db
@mark.parametrize(
    "data",
    [
        {"name": "Starship 1", "length": "12"},
        {"name": "Starship 2", "length": "12.56"},
    ],
)
def test_mutation_create_starship(
    graphql_client: GraphQLClient, snapshot: SnapshotTest, data: StarshipUpdateInput,
):
    with open(path.join(GRAPHQL_PATH, "mutation_create_starship.graphql")) as file:
        query = file.read()
        variables = {"data": data}
        response = graphql_client.execute(query, variable_values=variables)
        snapshot.assert_match(response)


@mark.django_db
@mark.parametrize(
    "data",
    [
        {"name": "Starhip Updated"},
        {"length": "12"},
        {"length": "12.00"},
        {"name": "Starship Updated", "length": "12"},
        {"name": "Starship Updated", "length": "12.00"},
    ],
)
def test_mutation_update_starship(
    graphql_client: GraphQLClient,
    starship_one: Starship,
    snapshot: SnapshotTest,
    data: StarshipUpdateInput,
):
    with open(path.join(GRAPHQL_PATH, "mutation_update_starship.graphql")) as file:
        query = file.read()
        starship_global_id = to_global_id(Starship.__name__, starship_one.id)
        variables = {"where": {"id": starship_global_id}, "data": data}
        response = graphql_client.execute(query, variable_values=variables)
        snapshot.assert_match(response)


@mark.django_db
def test_mutation_delete_starship(
    graphql_client: GraphQLClient, starship_one: Starship, snapshot: SnapshotTest
):
    with open(path.join(GRAPHQL_PATH, "mutation_delete_starship.graphql")) as file:
        query = file.read()
        starship_global_id = to_global_id(Starship.__name__, starship_one.id)
        variables = {"where": {"id": starship_global_id}}
        response = graphql_client.execute(query, variable_values=variables)
        snapshot.assert_match(response)
