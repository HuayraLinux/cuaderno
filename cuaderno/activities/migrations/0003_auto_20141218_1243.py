# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0002_auto_20141218_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='until_date',
            field=models.DateField(null=True, verbose_name='Until date', blank=True),
            preserve_default=True,
        ),
    ]
