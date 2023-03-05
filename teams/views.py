import json

from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView, DeleteView
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



class PlayerView(ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


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
