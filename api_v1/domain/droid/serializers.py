# Built-in packages

# Third-party packages
from rest_framework.serializers import ModelSerializer

# Local packages
from api_v1.domain.droid.models import Droid


class DroidSerializer(ModelSerializer):
    class Meta:
        model = Droid
        fields = "__all__"
