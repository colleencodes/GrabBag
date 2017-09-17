from rest_framework import serializers
from gifts.models import Gift, GiftAssignment

class GiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gift
        fields = ('id', 'title', 'description', 'link', 'photo')

class GiftAssignmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = GiftAssignment
		fields = ('grabbag_giver', 'grabbag_receiver', 'grabbag')
