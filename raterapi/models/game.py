from django.db import models


class Games(models.Model):

    name = models.CharField(max_length=75)
    title = models.CharField(max_length=75)
    description = models.CharField(max_length=125)
    year_released = models.IntegerField()
    number_of_players = models.IntegerField()
    estimated_time_play = models.IntegerField()
    age_recommendation = models.IntegerField()
