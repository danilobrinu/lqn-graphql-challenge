# Built-in packages

# Third-party packages
import django_filters as df

# Local packages
from api_v1.domain.person import models


class PersonFilter(df.FilterSet):
    first_name = df.CharFilter(field_name="first_name", lookup_expr="iexact")
    first_name_not = df.CharFilter(
        field_name="first_name", lookup_expr="iexact", exclude=True
    )
    first_name_contains = df.CharFilter(field_name="first_name", lookup_expr="contains")
    first_name_not_contains = df.CharFilter(
        field_name="first_name", lookup_expr="icontains", exclude=True
    )
    first_name_starts_with = df.CharFilter(
        field_name="first_name", lookup_expr="istartswith"
    )
    first_name_not_starts_with = df.CharFilter(
        field_name="first_name", lookup_expr="istartswith"
    )
    first_name_ends_with = df.CharFilter(field_name="first_name", lookup_expr="endswith")
    first_name_not_ends_with = df.CharFilter(
        field_name="first_name", lookup_expr="endswith", exclude=True
    )
    first_name_in = df.CharFilter(field_name="first_name", lookup_expr="in")
    first_name_not_in = df.CharFilter(
        field_name="first_name", lookup_expr="in", exclude=True
    )
    last_name = df.CharFilter(field_name="last_name", lookup_expr="iexact")
    last_name_not = df.CharFilter(
        field_name="last_name", lookup_expr="iexact", exclude=True
    )
    last_name_contains = df.CharFilter(field_name="last_name", lookup_expr="contains")
    last_name_not_contains = df.CharFilter(
        field_name="last_name", lookup_expr="icontains", exclude=True
    )
    last_name_starts_with = df.CharFilter(
        field_name="last_name", lookup_expr="istartswith"
    )
    last_name_not_starts_with = df.CharFilter(
        field_name="last_name", lookup_expr=["istartswith"]
    )
    last_name_ends_with = df.CharFilter(field_name="last_name", lookup_expr="endswith")
    last_name_not_ends_with = df.CharFilter(
        field_name="last_name", lookup_expr="endswith", exclude=True
    )
    last_name_in = df.CharFilter(field_name="last_name", lookup_expr="in")
    last_name_not_in = df.CharFilter(
        field_name="last_name", lookup_expr="in", exclude=True
    )

    class Meta:
        model = models.Person
        fields = []
