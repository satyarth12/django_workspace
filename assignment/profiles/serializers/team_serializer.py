from rest_framework import serializers
from profiles.models import Team


class TeamSerializer(serializers.RelatedField):

    def to_representation(self, value):
        return value.name

    class Meta:
        model = Team
        fields = ('name',)
