# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_auto_20141113_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=255, verbose_name='Name')),
                ('organizer', models.CharField(default=b'', max_length=255, verbose_name='Organizer')),
                ('location', models.CharField(default=b'', help_text='Province, city, venue.', max_length=255, verbose_name='Location')),
                ('day', models.DateField()),
                ('description', models.TextField(help_text='cantidad de asistentes, en que consistio, duracion, etc.')),
                ('authorities', models.TextField(verbose_name='Conectar Igualdad, ANSES, etc')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ActivityKind',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=255, verbose_name='Name')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ActivityURL',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='activity',
            name='kind',
            field=models.ForeignKey(to='activities.ActivityKind'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activity',
            name='staff',
            field=models.ManyToManyField(to='team.Member'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activity',
            name='urls',
            field=models.ManyToManyField(to='activities.ActivityURL'),
            preserve_default=True,
        ),
    ]
