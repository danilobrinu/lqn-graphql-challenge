# Built-in packages

# Third-party packages
from django_filters import FilterSet
from django_filters import CharFilter, NumberFilter

# Local packages
from . import models
from . import types


class DroidFilter(FilterSet):
    name = CharFilter(field_name="name", lookup_expr="iexact")
    name_not = CharFilter(field_name="name", lookup_expr="iexact", exclude=True)
    name_contains = CharFilter(field_name="name", lookup_expr="contains")
    name_not_contains = CharFilter(
        field_name="name", lookup_expr="icontains", exclude=True
    )
    name_starts_with = CharFilter(field_name="name", lookup_expr="istartswith")
    name_not_starts_with = CharFilter(field_name="name", lookup_expr="istartswith")
    name_ends_with = CharFilter(field_name="name", lookup_expr="endswith")
    name_not_ends_with = CharFilter(
        field_name="name", lookup_expr="endswith", exclude=True
    )
    name_in = CharFilter(field_name="name", lookup_expr="in")
    name_not_in = CharFilter(field_name="name", lookup_expr="in", exclude=True)
    primary_function = CharFilter(field_name="primary_function", lookup_expr="iexact")
    primary_function_not = CharFilter(
        field_name="primary_function", lookup_expr="iexact", exclude=True
    )
    primary_function_contains = CharFilter(
        field_name="primary_function", lookup_expr="contains"
    )
    primary_function_not_contains = CharFilter(
        field_name="primary_function", lookup_expr="icontains", exclude=True
    )
    primary_function_starts_with = CharFilter(
        field_name="primary_function", lookup_expr="istartswith"
    )
    primary_function_not_starts_with = CharFilter(
        field_name="primary_function", lookup_expr="istartswith"
    )
    primary_function_ends_with = CharFilter(
        field_name="primary_function", lookup_expr="endswith"
    )
    primary_function_not_ends_with = CharFilter(
        field_name="primary_function", lookup_expr="endswith", exclude=True
    )
    primary_function_in = CharFilter(field_name="primary_function", lookup_expr="in")
    primary_function_not_in = CharFilter(
        field_name="primary_function", lookup_expr="in", exclude=True
    )

    class Meta:
        model = models.Droid
        fields = []
