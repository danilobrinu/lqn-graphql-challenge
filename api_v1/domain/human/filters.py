# Built-in packages

# Third-party packages
import django_filters as df

# Local packages
from api_v1.domain.human import models


class HumanFilter(df.FilterSet):
    name = df.CharFilter(field_name="name", lookup_expr="iexact")
    name_not = df.CharFilter(field_name="name", lookup_expr="iexact", exclude=True)
    name_contains = df.CharFilter(field_name="name", lookup_expr="contains")
    name_not_contains = df.CharFilter(
        field_name="name", lookup_expr="icontains", exclude=True
    )
    name_starts_with = df.CharFilter(field_name="name", lookup_expr="istartswith")
    name_not_starts_with = df.CharFilter(field_name="name", lookup_expr="istartswith")
    name_ends_with = df.CharFilter(field_name="name", lookup_expr="endswith")
    name_not_ends_with = df.CharFilter(
        field_name="name", lookup_expr="endswith", exclude=True
    )
    name_in = df.CharFilter(field_name="name", lookup_expr="in")
    name_not_in = df.CharFilter(field_name="name", lookup_expr="in", exclude=True)

    class Meta:
        model = models.Human
        fields = []
