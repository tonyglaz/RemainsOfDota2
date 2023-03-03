from rest_framework import serializers


class PlayerSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nickname=serializers.CharField(max_length=100)
    status=serializers.CharField(max_length=11)
    team=serializers.CharField(max_length=100)