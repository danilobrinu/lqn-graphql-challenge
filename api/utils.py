# Built-in packages
from typing import Annotated, Any

# Third-party packages
from django.db.models import Model
from django.core.exceptions import ValidationError
from graphene_django.filter import DjangoFilterConnectionField

# Local packages


class BaseModel(Model):
    @staticmethod
    def create(
        self,
    ) -> Annotated[
        Any, "create a new object with the given data and returns that object"
    ]:
        self.save()

        return self

    @staticmethod
    def update(
        self, **kwargs
    ) -> Annotated[
        Any, "update a given object with the given data and returns that object"
    ]:
        for field, value in kwargs.items():
            setattr(self, field, value)
        self.save()

        return self

    @staticmethod
    def destroy(
        self,
    ) -> Annotated[Any, "delete a given object and returns that object"]:
        self.delete()

        return self

    class Meta:
        abstract = True


def create_open_crud_filter_connection(
    name, filterset_class
) -> Annotated[Any, "Custom DjangoFilterConnectionField for OpenCrud connections"]:
    @classmethod
    def resolve_queryset(
        cls, connection, iterable, info, args, filtering_args, **kwargs
    ):
        qs = super(DjangoFilterConnectionField, cls).resolve_queryset(
            connection, iterable, info, args
        )
        # To support open crud style
        filter_kwargs = args.get("where", {})
        filterset = filterset_class(
            data=filter_kwargs, queryset=qs, request=info.context
        )
        if filterset.form.is_valid():
            return filterset.qs
        raise ValidationError(filterset.form.errors.as_json())

    return type(
        name, (DjangoFilterConnectionField,), {"resolve_queryset": resolve_queryset}
    )
