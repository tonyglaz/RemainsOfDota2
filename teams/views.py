from django.db.models import Q
from django.http import HttpResponse
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet

from teams.models import Player, Team
from teams.serializers import PlayerSerializer, PlayerDetailSerializer, PlayerCreateSerializer, PlayerUpdateSerializer, \
    PlayerDestroySerializer, TeamSerializer


def hello(request):
    return HttpResponse("Hello world")


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class PlayerListView(ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    def get(self, request, *args, **kwargs):
        player_nickname = request.GET.get('nickname', None)
        if player_nickname:
            self.queryset = self.queryset.filter(
                nickname__icontains=player_nickname
            )
        team_names = request.GET.getlist('team', None)
        teams_q = None
        for team in team_names:
            if teams_q is None:
                teams_q = Q(team__name__icontains=team)
            else:
                teams_q |= Q(team__name__icontains=team)
        if teams_q:
            self.queryset = self.queryset.filter(teams_q)
        return super().get(request, *args, **kwargs)


class PlayerDetailView(RetrieveAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerDetailSerializer


class PlayerCreateView(CreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerCreateSerializer


class PlayerUpdateView(UpdateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerUpdateSerializer


class PlayerDeleteView(DestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerDestroySerializer
