# Built-in packages

# Third-party packages
from rest_framework.serializers import ModelSerializer

# Local packages
from api_v1.domain.starship.models import Starship


class StarshipSerializer(ModelSerializer):
    class Meta:
        model = Starship
        fields = "__all__"
