# Built-in packages

# Third-party packages
from rest_framework import serializers as drf_serializers

# Local packages
from api_v1.domain.episode.models import Episode


class EpisodeSerializer(drf_serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = "__all__"
