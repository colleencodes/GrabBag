from rest_framework import viewsets
from gifts.models import Gift, GiftAssignment
from gifts.serializer import GiftSerializer, GiftAssignmentSerializer

class GiftViewSet(viewsets.ModelViewSet):
    serializer_class = GiftSerializer
    queryset = Gift.objects.all()

class GiftAssignmentViewSet(viewsets.ModelViewSet):
	serializer_class = GiftAssignmentSerializer
	queryset = GiftAssignment.objects.all()
