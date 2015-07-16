# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bank',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='investor',
            options={'ordering': ('name',)},
        ),
        migrations.AddField(
            model_name='investor',
            name='banks',
            field=models.ManyToManyField(to='users.Bank'),
            preserve_default=True,
        ),
    ]
