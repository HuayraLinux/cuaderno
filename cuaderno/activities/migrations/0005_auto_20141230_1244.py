# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0004_activity_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='is_publised',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activityattachment',
            name='is_publised',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activity',
            name='owner',
            field=models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL, verbose_name='Owner'),
            preserve_default=True,
        ),
    ]
