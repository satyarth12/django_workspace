from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import NotFound, PermissionDenied, AuthenticationFailed
from django.contrib.auth import authenticate

from user.models import CustomUser


class CreateUserSerialzier(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password')

    def validate(self, attrs):
        email = attrs.get('email')
        username = attrs.get('username')
        password = attrs.get("password")

        # validation error if email exists in DB
        user_ = self.Meta.model.objects.filter(email=email, username=username)
        if user_.exists():
            raise serializers.ValidationError(
                "User with the email and username already exist")

        # validating password
        validate_password(password=password)

        return attrs

    def create(self, validated_data):
        """Creating User object.
        """
        # user object
        user_instance = self.Meta.model.objects.create_user(**validated_data)
        return user_instance


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=254)
    password = serializers.CharField()

    class Meta:
        model = CustomUser
        fields = ('email', 'password')

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        # validation error if email doesn't exists in DB
        user_ = self.Meta.model.objects.filter(email=email)
        if not user_.exists():
            raise NotFound(
                detail={"status": False, "message": "User with the email does not exist"}, code=404)

        # else part
        # authenticating user via credentials
        user = authenticate(email=email, password=password)

        if user is not None:
            if user.is_active:
                # adding and returning user to attrs dict
                attrs['user'] = user
                return attrs
            raise PermissionDenied(
                detail={"status": False, "message": "User Account is not active. Contact admin"}, code=403)

        raise AuthenticationFailed(
            detail={"status": False, "message": "Login credentials are incorrect"}, code=401)
