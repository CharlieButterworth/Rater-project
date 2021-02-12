from django.db import models


class Ratings(models.Model):

    rating = models.IntegerField()
    game = models.ForeignKey("Games", on_delete=models.CASCADE)
    player = models.ForeignKey("Players", on_delete=models.CASCADE)
