# Built-in packages

# Third-party packages
import rest_framework as drf

# Local packages
from api_v1.domain.starship.models import Starship


class StarshipSerializer(drf.serializers.ModelSerializer):
    class Meta:
        model = Starship
        fields = "__all__"
