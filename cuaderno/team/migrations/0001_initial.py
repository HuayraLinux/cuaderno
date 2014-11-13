# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_name', models.CharField(max_length=64, verbose_name='Last name')),
                ('first_name', models.CharField(max_length=64, verbose_name='First name')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
