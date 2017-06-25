from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    address = serializers.CharField(max_length=250)