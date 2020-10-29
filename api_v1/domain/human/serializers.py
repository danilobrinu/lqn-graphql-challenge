# Built-in packages

# Third-party packages
import rest_framework as drf

# Local packages
from api_v1.domain.human.models import Human


class HumanSerializer(drf.serializers.ModelSerializer):
    class Meta:
        model = Human
        fields = "__all__"
