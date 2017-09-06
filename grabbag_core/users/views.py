from rest_framework import viewsets
from users.models import User
from users.serializer import UserSerializer
from rest_framework.response import Response

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
