from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel
from rest_framework.authtoken.models import Token

from .managers import CustomUserManager


class User(AbstractUser, TimeStampedModel):
    contact_number = models.CharField(
        _('Contact No'), max_length=13, unique=True, default=None, null=True, )
    dob = models.DateField(blank=True, null=True)

    objects = CustomUserManager()

    REQUIRED_FIELDS = ['contact_number', ]

    class Meta:
        db_table = 'user'
        app_label = 'profiles'

    def __unicode__(self):
        return u'%s' % self.contact_number

User._meta.get_field("email").null = True


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
