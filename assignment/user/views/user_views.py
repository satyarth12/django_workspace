from rest_framework import permissions, generics, status, viewsets
from rest_framework.response import Response

from user.serializers.user_serializer import UserSerializer

from user.models import CustomUser


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    httP_method_names = ['GET', 'PATCH', 'PUT', 'HEAD', 'DELETE']

    def get_queryset(self):
        return CustomUser.objects.all()
