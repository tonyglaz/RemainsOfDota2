import json

from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from teams.models import Player


def hello(request):
    return HttpResponse("Hello world")


@method_decorator(csrf_exempt, name='dispatch')
class PlayerView(View):
    def get(self, request):
        players = Player.objects.all()
        search_nickname = request.GET.get('nickname', None)
        if search_nickname:
            players = players.filter(nickname=search_nickname)

        response = []
        for player in players:
            response.append({
                'id': player.id,
                'nickname': player.nickname
            })

        return JsonResponse(response, safe=False)

    def post(self, request):
        player_data = json.loads(request.body)
        player = Player()
        player.nickname = player_data['nickname']
        player.save()
        return JsonResponse({
            'id': player.id,
            'nickname': player.nickname
        }, safe=False)


class PlayerDetailView(DetailView):
    model = Player

    def get(self, request, *args, **kwargs):
        player = self.get_object()

        return JsonResponse({
            'id': player.id,
            'nickname': player.nickname
        }, safe=False)
