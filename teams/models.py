from django.db import models


class Tournament(models.Model):
    slug = models.SlugField(max_length=150)
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=1000)
    prize_pool = models.IntegerField(10)
    number_of_teams = models.IntegerField(8)


class Team(models.Model):
    slug = models.SlugField(max_length=50)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    tournament = models.ManyToManyField(Tournament, null=True)

    def __str__(self):
        return self.slug


class Player(models.Model):
    STATUS = [
        ('InTeam', "Играет в команде"),
        ('WithoutTeam', 'Без команды'),
        ('Resigned', 'Завершил карьеру')
    ]
    # TEAMS_BEFORE=[(Team.name)]

    slug = models.SlugField(max_length=50)
    nickname = models.CharField(max_length=100)
    status = models.CharField(max_length=11, choices=STATUS, default='WithoutTeam')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.slug
