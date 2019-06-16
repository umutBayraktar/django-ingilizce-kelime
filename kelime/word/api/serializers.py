from rest_framework.serializers import ModelSerializer

from ..models import Word

class WordSerializer(ModelSerializer):

    class Meta:
        model=Word
        fields=['lang_1','lang_2','image','is_active']
