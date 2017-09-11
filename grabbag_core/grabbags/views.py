from rest_framework import viewsets
from grabbags.models import Grabbag
from grabbags.serializer import GrabbagSerializer

class GrabbagViewSet(viewsets.ModelViewSet):
    serializer_class = GrabbagSerializer
    queryset = Grabbag.objects.all()
