from rest_framework import serializers

from teams.models import Player, Team


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"


class PlayerSerializer(serializers.ModelSerializer):
    team = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Player
        fields = ['nickname', 'team', 'status', 'slug']


class PlayerDetailSerializer(serializers.ModelSerializer):
    team = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name',
    )

    class Meta:
        model = Player
        fields = '__all__'


class PlayerCreateSerializer(serializers.ModelSerializer):
    team = serializers.SlugRelatedField(
        required=False,
        queryset=Team.objects.all(),
        slug_field='name',
    )

    class Meta:
        model = Player
        fields = '__all__'

    def is_valid(self, *, raise_exception=False):
        self._team = self.initial_data.pop("team")
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        player = Player.objects.create(**validated_data)
        player.save()
        return player


class PlayerUpdateSerializer(serializers.ModelSerializer):
    team = serializers.SlugRelatedField(
        required=False,
        queryset=Team.objects.all(),
        slug_field='name',
    )

    class Meta:
        model = Player
        fields = ['nickname', 'team', 'status', 'slug']

    def is_valid(self, *, raise_exception=False):
        self._team = self.initial_data.pop("team")
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        player = super().save()
        player.save()
        return player


class PlayerDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id']
