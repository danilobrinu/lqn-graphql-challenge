# Built-in packages

# Third-party packages
from django_filters import FilterSet
from django_filters import CharFilter

# Local packages
from . import models


class PersonFilter(FilterSet):
    first_name = CharFilter(field_name="first_name", lookup_expr="iexact")
    first_name_not = CharFilter(
        field_name="first_name", lookup_expr="iexact", exclude=True
    )
    first_name_contains = CharFilter(field_name="first_name", lookup_expr="contains")
    first_name_not_contains = CharFilter(
        field_name="first_name", lookup_expr="icontains", exclude=True
    )
    first_name_starts_with = CharFilter(
        field_name="first_name", lookup_expr="istartswith"
    )
    first_name_not_starts_with = CharFilter(
        field_name="first_name", lookup_expr="istartswith"
    )
    first_name_ends_with = CharFilter(field_name="first_name", lookup_expr="endswith")
    first_name_not_ends_with = CharFilter(
        field_name="first_name", lookup_expr="endswith", exclude=True
    )
    first_name_in = CharFilter(field_name="first_name", lookup_expr="in")
    first_name_not_in = CharFilter(
        field_name="first_name", lookup_expr="in", exclude=True
    )
    last_name = CharFilter(field_name="last_name", lookup_expr="iexact")
    last_name_not = CharFilter(
        field_name="last_name", lookup_expr="iexact", exclude=True
    )
    last_name_contains = CharFilter(field_name="last_name", lookup_expr="contains")
    last_name_not_contains = CharFilter(
        field_name="last_name", lookup_expr="icontains", exclude=True
    )
    last_name_starts_with = CharFilter(
        field_name="last_name", lookup_expr="istartswith"
    )
    last_name_not_starts_with = CharFilter(
        field_name="last_name", lookup_expr=["istartswith"]
    )
    last_name_ends_with = CharFilter(field_name="last_name", lookup_expr="endswith")
    last_name_not_ends_with = CharFilter(
        field_name="last_name", lookup_expr="endswith", exclude=True
    )
    last_name_in = CharFilter(field_name="last_name", lookup_expr="in")
    last_name_not_in = CharFilter(
        field_name="last_name", lookup_expr="in", exclude=True
    )

    class Meta:
        model = models.Person
        fields = []
