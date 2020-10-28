# Built-in packages

# Third-party packages
from django_filters import FilterSet, CharFilter, NumberFilter

# Local packages
from api_v1.utils.filters import NumberInFilter, CharInFilter
from api_v1.domain.starship import models


class StarshipFilter(FilterSet):
    name = CharFilter(field_name="name", lookup_expr="iexact")
    name_not = CharFilter(field_name="name", lookup_expr="iexact", exclude=True)
    name_contains = CharFilter(field_name="name", lookup_expr="icontains")
    name_not_contains = CharFilter(
        field_name="name", lookup_expr="icontains", exclude=True
    )
    name_starts_with = CharFilter(field_name="name", lookup_expr="istartswith")
    name_not_starts_with = CharFilter(field_name="name", lookup_expr="istartswith")
    name_ends_with = CharFilter(field_name="name", lookup_expr="iendswith")
    name_not_ends_with = CharFilter(
        field_name="name", lookup_expr="iendswith", exclude=True
    )
    name_in = CharInFilter(field_name="name", lookup_expr="in")
    name_not_in = CharInFilter(field_name="name", lookup_expr="in", exclude=True)
    length = NumberFilter(field_name="length", lookup_expr="exact")
    length_not = NumberFilter(field_name="length", lookup_expr="exact", exclude=True)
    length_lt = NumberFilter(field_name="length", lookup_expr="lt")
    length_lte = NumberFilter(field_name="length", lookup_expr="lte")
    length_gt = NumberFilter(field_name="length", lookup_expr="gt")
    length_gte = NumberFilter(field_name="length", lookup_expr="gte")
    length_in = NumberInFilter(field_name="length", lookup_expr="in")
    length_not_in = NumberInFilter(field_name="length", lookup_expr="in", exclude=True)

    class Meta:
        model = models.Starship
        fields = []
