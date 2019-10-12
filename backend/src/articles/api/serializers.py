from django.apps import apps
from rest_framework import serializers


class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('articles', 'Article')
        fields = ('title', 'content')