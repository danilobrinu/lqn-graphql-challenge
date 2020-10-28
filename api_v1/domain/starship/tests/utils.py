# Built-in packages
from typing import Dict

# Third-party packages
from faker import Faker

# Local packages
from api_v1.domain.starship.models import Starship
from api_v1.domain.starship.data import create_starship

faker = Faker()


def create_random_starship(overrides: dict = {}) -> Starship:
    starship = create_starship(
        {"name": faker.name(), "length": faker.pydecimal(2, 2, True)} | overrides
    )
    return starship
