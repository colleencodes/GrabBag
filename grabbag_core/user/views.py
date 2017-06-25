from rest_framework import viewsets
from user.models import User
from user.serializer import UserSerializer
from rest_framework.response import Response

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        serialized_list = UserSerializer(queryset)

        return Response(serialized_list.data)

