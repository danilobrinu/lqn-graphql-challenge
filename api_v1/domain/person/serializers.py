# Built-in packages

# Third-party packages
from rest_framework import serializers as drf_serializers

# Local packages
from api_v1.domain.person.models import Person


class PersonSerializer(drf_serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"
