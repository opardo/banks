from django.db import models

from numpy import eye, ones, vstack
from cvxopt import matrix, solvers


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
            c.append(float(-1-bank.interest_rate))
        c = matrix(c)
        return c

    def generate_A(self):
        m = len(self.banks.all())
        B = vstack((ones((1, m)), eye(m)))
        A = vstack((B, -1*eye(m)))
        A = matrix(A)
        return A

    def generate_b(self):

        b = [float(self.money)]
        for bank in self.banks.all():
            b.append(float(bank.upper_limit))
        for bank in self.banks.all():
            b.append(float(-bank.lower_limit))
        b = matrix(b)
        return b

    def solutions(self):

        sol = solvers.lp(self.generate_c(), self.generate_A(), self.generate_b())
        return sol





