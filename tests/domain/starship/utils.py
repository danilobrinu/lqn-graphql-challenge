# Built-in packages

# Third-party packages
from faker import Faker

# Local packages
from api.domain.starship.data import create_starship

faker = Faker()


def create_random_starship():
    starship = create_starship(
        {"name": faker.name(), "length": faker.pyfloat(2, 2, True)}
    )
    return starship
