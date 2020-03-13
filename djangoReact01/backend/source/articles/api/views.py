from rest_framework.generics import ListAPIView, RetrieveAPIView
from articles.models import Articles
from .serializers import ArticleSerializer


class ArticleListView(ListAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetailView(RetrieveAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer
