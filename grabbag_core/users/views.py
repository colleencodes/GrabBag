from rest_framework import viewsets
from users.models import User, Family
from users.serializer import UserSerializer, FamilySerializer

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class FamilyViewSet(viewsets.ModelViewSet):
	serializer_class = FamilySerializer
	queryset = Family.objects.all()
