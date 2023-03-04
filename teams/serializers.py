from rest_framework import serializers

from teams.models import Player


class PlayerSerializer(serializers.ModelSerializer):
    team=serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )
    class Meta:
        model = Player
        fields = ['nickname', 'team']


class PlayerDetailSerializer(serializers.ModelSerializer):
    team = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )
    class Meta:
        model = Player
        fields = '__all__'


class PlayerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Player
        exclude=['id']
