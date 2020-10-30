# Built-in packages

# Third-party packages
from rest_framework import serializers as drf_serializers

# Local packages
from api_v1.domain.planet.models import Planet


class PlanetSerializer(drf_serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = "__all__"
