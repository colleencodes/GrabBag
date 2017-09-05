from rest_framework import serializers
from user.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
    	model = User
    	fields = ('id', 'first_name', 'last_name', 'email', 'address', 'date_of_birth', 'is_adult')