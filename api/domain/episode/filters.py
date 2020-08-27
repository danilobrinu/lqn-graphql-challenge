# Built-in packages

# Third-party packages
from django_filters import FilterSet
from django_filters import CharFilter

# Local packages
from . import models


class EpisodeFilter(FilterSet):
    title = CharFilter(field_name="title", lookup_expr="iexact")
    title_not = CharFilter(field_name="title", lookup_expr="iexact", exclude=True)
    title_contains = CharFilter(field_name="title", lookup_expr="contains")
    title_not_contains = CharFilter(
        field_name="title", lookup_expr="icontains", exclude=True
    )
    title_starts_with = CharFilter(field_name="title", lookup_expr="istartswith")
    title_not_starts_with = CharFilter(field_name="title", lookup_expr="istartswith")
    title_ends_with = CharFilter(field_name="title", lookup_expr="endswith")
    title_not_ends_with = CharFilter(
        field_name="title", lookup_expr="endswith", exclude=True
    )
    title_in = CharFilter(field_name="title", lookup_expr="in")
    title_not_in = CharFilter(field_name="title", lookup_expr="in", exclude=True)

    class Meta:
        model = models.Episode
        fields = []
