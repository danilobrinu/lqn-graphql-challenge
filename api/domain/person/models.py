# Built-in packages

# Third-party package
from django.db import models

# Local packages
from api.utils.models import BaseModel


class Person(BaseModel):
    fist_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.first_name}, {self.last_name}"

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}:{self.id}>"
