from rest_framework import viewsets

from user.serializers.user_serializer import UserSerializer

from user.models import CustomUser
from user.permission import IsSameUserReadOnly


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (IsSameUserReadOnly,)
    http_method_names = ['get', 'patch', 'put', 'head', 'delete']

    def get_queryset(self):
        return CustomUser.objects.all()
