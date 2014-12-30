# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0005_auto_20141230_1244'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='is_publised',
            new_name='is_published',
        ),
        migrations.RenameField(
            model_name='activityattachment',
            old_name='is_publised',
            new_name='is_published',
        ),
    ]
