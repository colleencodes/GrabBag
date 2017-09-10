from rest_framework import viewsets
from gifts.models import Gift
from gifts.serializer import GiftSerializer

class GiftViewSet(viewsets.ModelViewSet):
    serializer_class = GiftSerializer
    queryset = Gift.objects.all()