# Built-in packages

# Third-party packages
import rest_framework as drf

# Local packages
from api_v1.domain.person.models import Person


class PersonSerializer(drf.serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"
