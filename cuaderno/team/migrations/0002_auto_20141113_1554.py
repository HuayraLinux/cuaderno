# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 13, 15, 54, 8, 889829), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 13, 15, 54, 18, 273573), auto_now=True),
            preserve_default=False,
        ),
    ]
