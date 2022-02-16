from rest_framework import serializers

from profiles.serializers.team_serializer import TeamSerializer
from profiles.models import Profile, Team


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('user', 'name', 'designation', 'profile_picture', 'team')
        read_only_fields = ('user',)
