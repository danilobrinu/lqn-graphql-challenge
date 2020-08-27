# Built-in packages

# Third-party packages
from django_filters import FilterSet
from django_filters import CharFilter

# Local packages
from . import models


class StarshipFilter(FilterSet):
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

    class Meta:
        model = models.Starship
        fields = []
