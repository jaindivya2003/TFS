from django.apps import apps
from rest_framework.generics import ListAPIView, RetrieveAPIView

# from articles.models import Article

from .serializers import ArticleSerializers

class ArticleListView(ListAPIView):
    queryset = apps.get_model('articles','Article').objects.all()
    serializer_class = ArticleSerializers

class ArticleDetailView(RetrieveAPIView):
    queryset = apps.get_model('articles','Article').objects.all()
    serializer_class = ArticleSerializers