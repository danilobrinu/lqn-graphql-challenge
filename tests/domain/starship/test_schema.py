# Built-in packages
from os import path

# Third-party packages
from pytest import fixture, mark
from graphql_relay import to_global_id
from graphene.test import Client
from config.schema import schema

# Local packages
from api.domain.starship.data import create_starship
from api.domain.starship.models import Starship

QUERIES_PATH = path.join(path.dirname(__file__), "queries")
MUTATION_PATH = path.join(path.dirname(__file__), "mutations")


@fixture
def starship_one():
    starship = create_starship({"name": "Starship One", "length": 11.00})
    return starship


@fixture
def starship_two():
    starship = create_starship({"name": "Starship Two", "length": 12.00})
    return starship


@fixture
def starship_three():
    starship = create_starship({"name": "Starship Three", "length": 13.00})
    return starship


@fixture
def graphql_client():
    client = Client(schema)
    return client


@mark.django_db
def test_query_starship(graphql_client: Client, starship_one, snapshot):
    with open(path.join(QUERIES_PATH, "query_get_starships.graphql")) as file:
        query = file.read()
        starship_global_id = to_global_id(Starship.__name__, starship_one.id)
        response = graphql_client.execute(query, {"id": starship_global_id})
        snapshot.assert_match(response)


@mark.django_db
def test_query_starships(
    graphql_client: Client, starship_one, starship_two, starship_three, snapshot
):
    with open(path.join(QUERIES_PATH, "query_get_starships.graphql")) as file:
        query = file.read()
        response = graphql_client.execute(query)
        snapshot.assert_match(response)
