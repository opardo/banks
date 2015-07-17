# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150716_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='interest_rate',
            field=models.DecimalField(default=0, max_digits=5, decimal_places=2),
        ),
    ]
