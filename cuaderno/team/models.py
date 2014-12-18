from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.

class Member(models.Model):
    last_name = models.CharField(max_length=64,
                                 verbose_name=_('Last name'))
    first_name = models.CharField(max_length=64,
                                  verbose_name=_('First name'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s, %s' % (self.last_name, self.first_name)

    class Meta:
        verbose_name = _('Member')
        verbose_name_plural = _('Members')
