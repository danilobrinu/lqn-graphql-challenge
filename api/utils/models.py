# Built-in packages
from typing import Any

# Third-party packages
from django.db.models import Model

# Local packages


class BaseModel(Model):
    def create(self,) -> Any:
        self.id = None
        self.save()

        return self

    def update(self, **kwargs) -> Any:
        for field, value in kwargs.items():
            setattr(self, field, value)
        self.save()

        return self

    def destroy(self,) -> Any:
        self.delete()

        return self

    class Meta:
        abstract = True
