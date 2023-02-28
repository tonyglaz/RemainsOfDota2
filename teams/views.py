import json

from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from teams.models import Player


def hello(request):
    return HttpResponse("Hello world")


class PlayerView(ListView):
    model = Player

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)  # у self появляется object_list где есть все игроки
        search_nickname = request.GET.get('nickname', None)
        if search_nickname:
            self.object_list = self.object_list.filter(nickname=search_nickname)

        response = []
        for player in self.object_list:
            response.append({
                'id': player.id,
                'nickname': player.nickname
            })

        return JsonResponse(response, safe=False)


class PlayerDetailView(DetailView):
    model = Player

    def get(self, request, *args, **kwargs):
        player = self.get_object()

        return JsonResponse({
            'id': player.id,
            'nickname': player.nickname
        }, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class PlayerCreateView(CreateView):
    model = Player
    fields = ['slug', 'nickname', 'status', 'team']

    def post(self, request):
        player_data = json.loads(request.body)

        player = Player.objects.create(
          #  player_id=player_data['player_id'],
            slug=player_data['slug'],
            nickname=player_data['nickname'],
            status=player_data['status']
            #team=player_data['team']
        )

        player.save()
        return JsonResponse({
            'id': player.id,
            'nickname': player.nickname
        }, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class PlayerUpdateView(UpdateView):
    model = Player
    fields = ['slug', 'nickname', 'status', 'team']

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        player_data = json.loads(request.body)
       # self.player_id = player_data['player_id']
        self.slug = player_data['slug']
        self.nickname = player_data['nickname']
        self.status = player_data['status']
      #  self.team = player_data['team']
        return JsonResponse({
         #   'id': self.object.id,
            'nickname': self.object.nickname,
            'status': self.object.status,
         #   'team': self.object.team,
            'slug': self.object.slug,
        }, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class PlayerDeleteView(DeleteView):
    model = Player
    success_url = '/player'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)
