from django.db import models

from cvxopt import matrix


class Bank(models.Model):
    name = models.CharField(max_length=200)
    lower_limit = models.IntegerField(default=0)
    upper_limit = models.IntegerField(default=0)
    interest_rate = models.DecimalField(default=0, max_digits=5, decimal_places=2)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Investor(models.Model):
    name = models.CharField(max_length=200)
    money = models.IntegerField(default=0)
    banks = models.ManyToManyField(Bank)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)

    def generate_c(self):

        c = []

        for bank in self.banks.all():
            c.append(float(1+bank.interest_rate))

        c = matrix (c)

        return c

