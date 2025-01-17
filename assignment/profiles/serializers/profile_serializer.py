from rest_framework import serializers

from profiles.serializers.team_serializer import TeamSerializer
from profiles.models import Profile, Team


class ProfileSerializer(serializers.ModelSerializer):

    profile_team = serializers.ListField(
        required=False, help_text="Team object id. Ex: 1")

    class Meta:
        model = Profile
        fields = ('user', 'name', 'designation',
                  'profile_picture', 'profile_team')
        read_only_fields = ('user',)
