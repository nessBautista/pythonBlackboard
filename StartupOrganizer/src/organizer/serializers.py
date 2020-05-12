from rest_framework.serializers import ModelSerializer
from .models import NewsLink, Startup, Tag


class TagSerializer(ModelSerializer):
    """Serialize Tag data"""

    class Meta:
        model = Tag
        fields = "__all__"


class StartupSerializer(ModelSerializer):
    """Serialize Startup data"""

    tags = TagSerializer(many=True)

    class Meta:
        model = Startup
        fields = "__all__"


class NewsLinkSerializer(ModelSerializer):
    """Serialize NewsLink data"""

    startup = StartupSerializer()

    class Meta:
        model = NewsLink
        fields = "__all__"
