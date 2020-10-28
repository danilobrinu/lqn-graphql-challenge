# Built-in packages

# Third-party packages
from faker import Faker

# Local packages
from api_v1.domain.human.models import Human
from api_v1.domain.human.data import create_human

faker = Faker()


def create_random_human() -> Human:
    human = create_human(
        {"name": faker.name(), "appears_in": [], "home_planet": "Earth", "friends": []}
    )
    return human
