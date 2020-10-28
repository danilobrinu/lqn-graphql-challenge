# Built-in packages

# Third-party packages
from django.forms import DecimalField, CharField
from django_filters.filters import Filter

# Local packages


class BaseInFilter(Filter):
    def __init__(_, *args, **kwargs):
        kwargs.setdefault("lookup_expr", "in")
        super().__init__(*args, **kwargs)

    def to_python(self, value):
        return self._field_class().to_python(value)

    def sanitize_value(self, value):
        return list(map(lambda v: self.to_python(v), value))

    def filter(self, qs, value):
        if value is None:
            return super().filter(qs, [])

        return super().filter(qs, self.sanitize_value(value))


class NumberInFilter(BaseInFilter):
    _field_class = DecimalField


class CharInFilter(BaseInFilter):
    _field_class = CharField

