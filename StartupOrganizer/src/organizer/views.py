from django.http import HttpResponse
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
)

# from rest_framework.renderers import JSONRenderer
# from django.views import View
from .serializers import StartupSerializer, TagSerializer, NewsLinkSerializer
from .models import Startup, Tag, NewsLink


class TagApiDetail(RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = "slug"


class TagApiList(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class StartupAPIDetail(RetrieveAPIView):
    queryset = Startup.objects.all()
    serializer_class = StartupSerializer
    lookup_field = "slug"


class StartupAPIList(ListAPIView):
    queryset = Startup.objects.all()
    serializer_class = StartupSerializer


class NewsLinkAPIDetail(RetrieveAPIView):
    queryset = NewsLink.objects.all()
    serializer_class = NewsLinkSerializer

    def get_object(self):
        """Override DRF's generic Method2
        """
        startup_slug = self.kwargs.get("startup_slug")
        newslink_slug = self.kwargs.get("newslink_slug")

        queryset = self.filter_queryset(self.get_queryset())

        newslink = get_object_or_404(
            queryset, slug=newslink_slug, startup__slug=startup_slug,
        )
        self.check_object_permissions(self.request, newslink)
        return newslink


class NewsLinkAPIList(ListAPIView):
    queryset = NewsLink.objects.all()
    serializer_class = NewsLinkSerializer
