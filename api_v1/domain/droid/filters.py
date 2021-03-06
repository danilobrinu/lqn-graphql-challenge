# Built-in packages

# Third-party packages
import django_filters as df

# Local packages
from api_v1.domain.droid import models


class DroidFilter(df.FilterSet):
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
    primary_function = df.CharFilter(field_name="primary_function", lookup_expr="iexact")
    primary_function_not = df.CharFilter(
        field_name="primary_function", lookup_expr="iexact", exclude=True
    )
    primary_function_contains = df.CharFilter(
        field_name="primary_function", lookup_expr="contains"
    )
    primary_function_not_contains = df.CharFilter(
        field_name="primary_function", lookup_expr="icontains", exclude=True
    )
    primary_function_starts_with = df.CharFilter(
        field_name="primary_function", lookup_expr="istartswith"
    )
    primary_function_not_starts_with = df.CharFilter(
        field_name="primary_function", lookup_expr="istartswith"
    )
    primary_function_ends_with = df.CharFilter(
        field_name="primary_function", lookup_expr="endswith"
    )
    primary_function_not_ends_with = df.CharFilter(
        field_name="primary_function", lookup_expr="endswith", exclude=True
    )
    primary_function_in = df.CharFilter(field_name="primary_function", lookup_expr="in")
    primary_function_not_in = df.CharFilter(
        field_name="primary_function", lookup_expr="in", exclude=True
    )

    class Meta:
        model = models.Droid
        fields = []
