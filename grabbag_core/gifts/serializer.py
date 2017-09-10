from rest_framework import serializers
from gifts.models import Gift

class GiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gift
        fields = ('id', 'title', 'description', 'link', 'photo')
