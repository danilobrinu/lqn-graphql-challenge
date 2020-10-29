# Built-in packages

# Third-party packages
import django_filters as df

# Local packages
from api_v1.domain.episode import models


class EpisodeFilter(df.FilterSet):
    title = df.CharFilter(field_name="title", lookup_expr="iexact")
    title_not = df.CharFilter(field_name="title", lookup_expr="iexact", exclude=True)
    title_contains = df.CharFilter(field_name="title", lookup_expr="contains")
    title_not_contains = df.CharFilter(
        field_name="title", lookup_expr="icontains", exclude=True
    )
    title_starts_with = df.CharFilter(field_name="title", lookup_expr="istartswith")
    title_not_starts_with = df.CharFilter(field_name="title", lookup_expr="istartswith")
    title_ends_with = df.CharFilter(field_name="title", lookup_expr="endswith")
    title_not_ends_with = df.CharFilter(
        field_name="title", lookup_expr="endswith", exclude=True
    )
    title_in = df.CharFilter(field_name="title", lookup_expr="in")
    title_not_in = df.CharFilter(field_name="title", lookup_expr="in", exclude=True)

    class Meta:
        model = models.Episode
        fields = []
