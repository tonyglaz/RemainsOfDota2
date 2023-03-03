from rest_framework import serializers

from teams.models import Player


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['nickname', 'team']


class PlayerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'
