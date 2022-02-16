from rest_framework import permissions, generics, status, views
from rest_framework.response import Response

from django.contrib.auth import login

from user.serializers.auth_serializer import CreateUserSerialzier, LoginSerializer
from user.serializers.user_serializer import UserSerializer

from user.models import CustomUser


class RegisterView(generics.GenericAPIView):
    serializer_class = CreateUserSerialzier
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        data = request.data

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # auth token for user
        token = user.create_auth_token

        return Response({"status": True,
                         "detail": {"user_info": UserSerializer(user).data, "token": token}
                         }, status=status.HTTP_201_CREATED)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        data = request.data

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']

        # logging the user
        login(request, user)

        # creating auth token
        token = user.create_auth_token
        return Response({"status": True,
                         "detail": {"user_info": UserSerializer(user).data, "token": token}
                         }, status=status.HTTP_201_CREATED)


class LogoutView(views.APIView):

    def post(self, request):
        # deleting the auth token of user
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
