from django.db import models
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
# Create your models here.

class Source(models.Model):
    user = models.ForeignKey(User, verbose_name=_("user"), on_delete=models.CASCADE)
    name = models.CharField(_("name"), max_length=50)

    class Meta:
        unique_together = ['user', 'name']

    def __str__(self):
        return self.name


class Event(models.Model):
    COLOR_CHOICES = (
      (0, ('primary')),
      (1, _('success')),
      (2, _('danger')),
      (3, _('warning')),
      (4, _('dark')),
    )
    source   =  models.ForeignKey(Source,related_name='events',
                    verbose_name=_("source"),
                    on_delete=models.CASCADE)
    date     =  models.DateField(_("date"),  auto_now_add=False)
    color    =  models.PositiveSmallIntegerField(choices=COLOR_CHOICES)

    class Meta:
        unique_together = ['source', 'date']

    def __str__(self):
        return f'{self.source} - {self.date}'
