# Built-in packages

# Third-party packages
from rest_framework.serializers import ModelSerializer

# Local packages
from api_v1.domain.human.models import Human


class HumanSerializer(ModelSerializer):
    class Meta:
        model = Human
        fields = "__all__"
