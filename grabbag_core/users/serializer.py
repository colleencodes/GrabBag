from rest_framework import serializers
from users.models import User, Family, UserGift

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'address', 'date_of_birth', 'is_adult')

class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = ('id', 'name', 'members')

class UserGiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGift
        fields = ('user', 'gift', 'grabbag')
