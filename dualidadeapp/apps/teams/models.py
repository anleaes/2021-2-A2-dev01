from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Team(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField('Nome', max_length=50)
    user_team = models.ManyToManyField(User, through='TeamUser', blank=True)
    
    class Meta:
        verbose_name = 'Equipe'
        verbose_name_plural = 'Equipes'
        ordering =['id']

    def __str__(self):
        return self.name


class TeamUser(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Formação de equipe'
        verbose_name_plural = 'Formação de equipes'
        ordering =['id']

    def __str__(self):
        return self.team.name