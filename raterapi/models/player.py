from django.db import models


class Players(model.Model):

    user = models.models.ForeignKey("User", on_delete=models.CASCADE)
