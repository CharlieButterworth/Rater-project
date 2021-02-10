from django.db import models


class Users(model.Model):

    firstName = models.CharField(max_length=75)
    lastName = models.CharField(max_length=75)
    email = models.CharField(max_length=75)
    password = models.CharField(max_length=75)
