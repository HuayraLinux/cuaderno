from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class ActivityURL(models.Model):
    url = models.URLField()


class ActivityKind(models.Model):
    name = models.CharField(max_length=255,
                            default='',
                            verbose_name=_('Name'))

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        ordering = ['name']
        verbose_name = _('Kind of activity')
        verbose_name_plural = _('Kinds of activity')


class Activity(models.Model):
    kind = models.ForeignKey('ActivityKind', verbose_name=_('Kind'))

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

    day = models.DateField(verbose_name=_('Day'))

    description = models.TextField(verbose_name=_('Description'),
                                   help_text=_('cantidad de asistentes, en que consistio, duracion, etc.'))

    authorities = models.TextField(verbose_name=_('Authorities'),
                                   help_text=_('Conectar Igualdad, ANSES, etc'))

    staff = models.ManyToManyField('team.Member')

    urls = models.ManyToManyField('ActivityURL')

    attachments = models.ManyToManyField('attachments.Attachment')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Activity')
        verbose_name_plural = _('Activities')
