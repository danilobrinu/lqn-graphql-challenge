# Built-in packages

# Third-party packages
from rest_framework import serializers as drf_serializers

# Local packages
from api_v1.domain.droid.models import Droid


class DroidSerializer(drf_serializers.ModelSerializer):
    class Meta:
        model = Droid
        fields = "__all__"
