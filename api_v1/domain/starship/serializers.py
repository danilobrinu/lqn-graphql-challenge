# Built-in packages

# Third-party packages
from rest_framework import serializers as drf_serializers


# Local packages
from api_v1.domain.starship.models import Starship


class StarshipSerializer(drf_serializers.ModelSerializer):
    class Meta:
        model = Starship
        fields = "__all__"
