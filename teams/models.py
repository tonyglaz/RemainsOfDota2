from django.db import models


class Player(models.Model):
    STATUS = [
        ('InTeam', "Играет в команде"),
        ('WithoutTeam', 'Без команды'),
        ('Resigned', 'Завершил карьеру')
    ]

    slug = models.SlugField(max_length=50)
    nickname = models.CharField(max_length=100)
    status = models.CharField(max_length=11, choices=STATUS, default='WithoutTeam')

    def __str__(self):
        return self.slug
