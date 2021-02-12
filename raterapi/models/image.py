from django.db import models


class Images(models.Model):

    image = models.ImageField(
        (""), upload_to=None, height_field=None, width_field=None, max_length=None)
    player = models.ForeignKey(
        "Players", on_delete=models.CASCADE)
