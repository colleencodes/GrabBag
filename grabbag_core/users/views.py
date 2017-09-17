from rest_framework import viewsets
from users.models import User, Family, UserGift
from users.serializer import UserSerializer, FamilySerializer, UserGiftSerializer

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class FamilyViewSet(viewsets.ModelViewSet):
	serializer_class = FamilySerializer
	queryset = Family.objects.all()

class UserGiftViewSet(viewsets.ModelViewSet):
	serializer_class = UserGiftSerializer
	queryset = UserGift.objects.all()
