from rest_framework import viewsets
from profiles.serializers.team_serializer import TeamSerializer
from profiles.models import Team


class TeamView(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
    http_method_names = ['get', 'post']
