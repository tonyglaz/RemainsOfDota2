import json

from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView, DeleteView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from teams.models import Player
from teams.serializers import PlayerSerializer, PlayerDetailSerializer, PlayerCreateSerializer, PlayerUpdateSerializer, \
    PlayerDestroySerializer


def hello(request):
    return HttpResponse("Hello world")


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
