from django.db import models


class GameCategories(models.Model):

    category = models.ForeignKey("Categories", on_delete=models.CASCADE)
    game = models.ForeignKey("Games", on_delete=models.CASCADE)
