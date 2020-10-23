# Built-in packages
from typing import Annotated, Any

# Third-party packages
from django.db.models import Model

# Local packages


class BaseModel(Model):
    def create(
        self,
    ) -> Annotated[
        Any, "create a new object with the given data and returns that object"
    ]:
        self.id = None
        self.pk = None
        self.save()

        return self

    def update(
        self, **kwargs
    ) -> Annotated[
        Any, "update a given object with the given data and returns that object"
    ]:
        for field, value in kwargs.items():
            setattr(self, field, value)
        self.save()

        return self

    def destroy(
        self,
    ) -> Annotated[Any, "delete a given object and returns that object"]:
        self.delete()

        return self

    class Meta:
        abstract = True
