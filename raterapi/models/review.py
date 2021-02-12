from django.db import models


class Reviews(models.Model):

    content = models.CharField(max_length=75)
    player = models.ForeignKey("Players", on_delete=models.CASCADE)
