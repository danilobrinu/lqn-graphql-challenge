# Built-in packages

# Third-party package
from django.db import models

# Local packages
from ...utils import BaseModel


class Person(BaseModel):
    fist_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"

    def __repr__(self):
        return f"<Person:{self.id}>"
