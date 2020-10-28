# Built-in packages

# Third-party packages
from rest_framework.serializers import ModelSerializer

# Local packages
from api_v1.domain.person.models import Person


class PersonSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"
