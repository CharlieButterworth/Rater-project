from django.db import models


class Ratings(models.Model):

    rating = models.models.IntegerField()
    game = models.models.ForeignKey("Games", on_delete=models.CASCADE)
    player = models.models.ForeignKey("Players", on_delete=models.CASCADE)
