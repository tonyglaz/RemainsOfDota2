import json

from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from django.forms.models import model_to_dict

from RemainsOfDota2 import settings
from teams.models import Player
from teams.serializers import PlayerSerializer, PlayerDetailSerializer, PlayerCreateSerializer


def hello(request):
    return HttpResponse("Hello world")


class PlayerView(ListView):
    model = Player

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)  # у self появляется object_list где есть все игроки
        search_nickname = request.GET.get('nickname', None)
        if search_nickname:
            self.object_list = self.object_list.filter(nickname=search_nickname)

        self.object_list=self.object_list.order_by('team')

        paginator=Paginator(self.object_list,settings.TOTAL_ON_PAGE)
        page_number=request.GET.get("page")
        page_obj=paginator.get_page(page_number)

        # players=[]
        # for player in page_obj:
        #     players.append({
        #         'id': player.id,
        #         'nickname': player.nickname,
        #         'team': player.team.name,
        #         'status': player.status
        #     })

       # list(map(lambda x: setattr(x,"team",x.team.name if x.team else None),page_obj))
        response = {
            "items":PlayerSerializer(page_obj,many=True).data,
            "num_pages":paginator.num_pages,
            "total":paginator.count
        }

        return JsonResponse(response, safe=False)


class PlayerDetailView(DetailView):
    model = Player

    def get(self, request, *args, **kwargs):
        player = self.get_object()

        return JsonResponse(PlayerDetailSerializer(player).data)


@method_decorator(csrf_exempt, name='dispatch')
class PlayerCreateView(CreateView):
    model = Player
    fields = ['slug', 'nickname', 'status', 'team']

    def post(self, request):
        player_data = PlayerCreateSerializer(data=json.loads(request.body))
        if player_data.is_valid():
            player_data.save()
        else:
            return JsonResponse(player_data.errors)
        # player = Player.objects.create(
        #     #  player_id=player_data['player_id'],
        #     slug=player_data['slug'],
        #     nickname=player_data['nickname'],
        #     status=player_data['status'],
        #     team=player_data['team']
        # )
        #
        # player.save()
        return JsonResponse(player_data.data)

@method_decorator(csrf_exempt, name='dispatch')
class PlayerUpdateView(UpdateView):
    model = Player
    fields = ['slug', 'nickname', 'status', 'team']

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        player_data = json.loads(request.body)
        self.slug = player_data['slug']
        self.nickname = player_data['nickname']
        self.status = player_data['status']
        self.team.name = player_data['team']

        # for skill in player_data:
        #     try:
        #         skill_obj=Player.objects.get(name=skill)
        #     except Player.DoesNotExist:
        #         return JsonResponse({"error":"skill not found"})
        #     self.object.player.add(skill_obj)
        #  self.team = player_data['team']
        return JsonResponse({
            #   'id': self.object.id,
            'nickname': self.object.nickname,
            'status': self.object.status,
            'team': self.object.team.name,
            'slug': self.object.slug,
        }, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class PlayerDeleteView(DeleteView):
    model = Player
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)
