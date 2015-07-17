# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20150716_2040'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='investor',
            options={'ordering': ('-register_date',)},
        ),
        migrations.AddField(
            model_name='investor',
            name='register_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
    ]
