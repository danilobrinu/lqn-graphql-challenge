# Built-in packages

# Third-party packages
from rest_framework.serializers import ModelSerializer

# Local packages
from api_v1.domain.planet.models import Planet


class PlanetSerializer(ModelSerializer):
    class Meta:
        model = Planet
        fields = "__all__"
