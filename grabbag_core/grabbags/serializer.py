from rest_framework import serializers
from grabbags.models import Grabbag

class GrabbagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grabbag
        fields = ('id', 'date', 'address', 'num_participating')
