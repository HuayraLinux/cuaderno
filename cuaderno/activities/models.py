
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cuaderno.storage import OwnCloudStorage

# Create your models here.

oc = OwnCloudStorage()


class ActivityURL(models.Model):
    activity = models.ForeignKey('Activity')
    url = models.URLField()

    class Meta:
        verbose_name = _('URL')
        verbose_name_plural = _('URLs')


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


class ActivityAttachment(models.Model):
    activity = models.ForeignKey('Activity')
    data = models.FileField(storage=oc, upload_to='/huayra-cuaderno/actividades/')
    #data = models.FileField(upload_to='/huayra-cuaderno/actividades/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Attachment')
        verbose_name_plural = _('Attachments')



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

    from_date = models.DateField(verbose_name=_('From date'))
    until_date = models.DateField(verbose_name=_('Until date'), blank=True, null=True)

    description = models.TextField(verbose_name=_('Description'),
                                   help_text=_('cantidad de asistentes, en que consistio, duracion, etc.'))

    authorities = models.TextField(verbose_name=_('Authorities'),
                                   help_text=_('Conectar Igualdad, ANSES, etc'))

    staff = models.ManyToManyField('team.Member')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(User, editable=False, verbose_name=_('Owner'))

    def __unicode__(self):
        return u'%s (%s)' % (self.name, self.organizer)

    class Meta:
        verbose_name = _('Activity')
        verbose_name_plural = _('Activities')
