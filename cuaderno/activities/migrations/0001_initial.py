# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_auto_20141218_1157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=255, verbose_name='Name')),
                ('organizer', models.CharField(default=b'', max_length=255, verbose_name='Organizer')),
                ('location', models.CharField(default=b'', help_text='Province, city, venue.', max_length=255, verbose_name='Location')),
                ('day', models.DateField(verbose_name='Day')),
                ('description', models.TextField(help_text='cantidad de asistentes, en que consistio, duracion, etc.', verbose_name='Description')),
                ('authorities', models.TextField(help_text='Conectar Igualdad, ANSES, etc', verbose_name='Authorities')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Activity',
                'verbose_name_plural': 'Activities',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ActivityAttachment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.FileField(upload_to=b'/huayra-cuaderno/actividades/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('activity', models.ForeignKey(to='activities.Activity')),
            ],
            options={
                'verbose_name': 'Attachment',
                'verbose_name_plural': 'Attachments',
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
                'ordering': ['name'],
                'verbose_name': 'Kind of activity',
                'verbose_name_plural': 'Kinds of activity',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ActivityURL',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField()),
                ('activity', models.ForeignKey(to='activities.Activity')),
            ],
            options={
                'verbose_name': 'URL',
                'verbose_name_plural': 'URLs',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='activity',
            name='kind',
            field=models.ForeignKey(verbose_name='Kind', to='activities.ActivityKind'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activity',
            name='staff',
            field=models.ManyToManyField(to='team.Member'),
            preserve_default=True,
        ),
    ]
