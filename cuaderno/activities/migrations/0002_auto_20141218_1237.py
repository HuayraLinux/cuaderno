# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='day',
        ),
        migrations.AddField(
            model_name='activity',
            name='from_date',
            field=models.DateField(default=datetime.date(1900, 1, 1), verbose_name='From date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='activity',
            name='until_date',
            field=models.DateField(default=datetime.date(1900, 1, 1), verbose_name='Until date', blank=True),
            preserve_default=False,
        ),
    ]
