# Built-in packages

# Third-party packages
import rest_framework as drf

# Local packages
from api_v1.domain.droid.models import Droid


class DroidSerializer(drf.serializers.ModelSerializer):
    class Meta:
        model = Droid
        fields = "__all__"
