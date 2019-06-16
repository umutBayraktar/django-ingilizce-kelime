from rest_framework.viewsets import ModelViewSet
from ..models import Word
from .serializers import WordSerializer

class WordViewSet(ModelViewSet):

    serializer_class = WordSerializer
    queryset = Word.objects.all()



