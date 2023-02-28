from django.db import models


class Tournament(models.Model):
    slug = models.SlugField(max_length=150)
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=1000, null=True)
    prize_pool = models.IntegerField(verbose_name="Призовой фонд")
    number_of_teams = models.IntegerField(verbose_name="Количество команд")

    class Meta:
        verbose_name = "Турнир"
        verbose_name_plural = "Турниры"

    def __str__(self):
        return self.slug


class Team(models.Model):
    slug = models.SlugField(max_length=50)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    tournaments = models.ManyToManyField(Tournament)

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"

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

    class Meta:
        verbose_name = "Игрок"
        verbose_name_plural = "Игроки"

    def __str__(self):
        return self.slug
