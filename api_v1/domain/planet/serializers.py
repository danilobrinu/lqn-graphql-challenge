# Built-in packages

# Third-party packages
import rest_framework as drf

# Local packages
from api_v1.domain.planet.models import Planet


class PlanetSerializer(drf.serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = "__all__"
