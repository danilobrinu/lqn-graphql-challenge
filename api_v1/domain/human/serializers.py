# Built-in packages

# Third-party packages
from rest_framework import serializers as drf_serializers

# Local packages
from api_v1.domain.human.models import Human


class HumanSerializer(drf_serializers.ModelSerializer):
    class Meta:
        model = Human
        fields = "__all__"
