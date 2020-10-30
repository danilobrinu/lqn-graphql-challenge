# Built-in packages
from typing import Annotated, Any

# Third-party packages
from django.core.exceptions import ValidationError
from graphene.relay import Node as RelayNode
from graphene_django.filter import DjangoFilterConnectionField

# Local packages


def create_open_crud_filter_connection_field(
    name, filterset_class
) -> Annotated[Any, "OpenCrudFilterConnectionField"]:
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

