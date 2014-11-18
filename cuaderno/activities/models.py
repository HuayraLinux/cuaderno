from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.

class ActivityURL(models.Model):
    url = models.URLField()


class Activity(models.Model):
    KIND_CHOICES = (
        ('charla', _('Conference')),
        ('taller', _('Workshop')),
        ('stand', _('Stand')),
    )

    kind = models.CharField(max_length=10,
                            choices=KIND_CHOICES,
                            verbose_name=_('Kind'))

    name = models.CharField(max_length=255,
                            default='',
                            verbose_name=_('Name'))

    organizer = models.CharField(max_length=255,
                            default='',
                            verbose_name=_('Organizer'))

    location = models.CharField(max_length=255,
                                default='',
                                verbose_name=_('Location'),
                                help_text=_('Province, city, venue.'))

    day = models.DateField()

    description = models.TextField(
                                   help_text=_('cantidad de asistentes, en que consistio, duracion, etc.'))

    authorities = models.TextField(
                                   _('Conectar Igualdad, ANSES, etc'))

    staff = models.ManyToManyField('team.Member')

    urls = models.ManyToManyField('ActivityURL')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
