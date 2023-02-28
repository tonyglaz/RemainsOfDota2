from django.contrib import admin

from teams.models import Player, Team, Tournament

admin.site.register([Player, Team, Tournament])
