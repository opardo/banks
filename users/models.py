from django.db import models

class Investor(models.Model):
    name = models.CharField(max_length=200)
    money = models.IntegerField(default=0)


class Bank(models.Model):
    name = models.CharField(max_length=200)
    lower_limit = models.IntegerField(default=0)
    upper_limit = models.IntegerField(default=0)
    interest_rate = models.DecimalField(default=0, max_digits=5, decimal_places=3)
