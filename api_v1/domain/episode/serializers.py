# Built-in packages

# Third-party packages
from rest_framework.serializers import ModelSerializer

# Local packages
from api_v1.domain.episode.models import Episode


class EpisodeSerializer(ModelSerializer):
    class Meta:
        model = Episode
        fields = "__all__"
