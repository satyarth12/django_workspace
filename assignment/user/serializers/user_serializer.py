from rest_framework import serializers
from user.models import CustomUser


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')
