# Built-in packages

# Third-party packages
import rest_framework as drf

# Local packages
from api_v1.domain.episode.models import Episode


class EpisodeSerializer(drf.serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = "__all__"
