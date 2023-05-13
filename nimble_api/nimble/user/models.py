from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.utils import timezone
from uuid import uuid4

from nimble.common.models import Base
from .constants import AccountType, ActivityType


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    return 'avatar/{}/{}.{}'.format(instance.pk, uuid4(), ext)


class User(AbstractUser):
    account_type = models.PositiveIntegerField(
        verbose_name=_('AccountType'),
        choices=AccountType.choices,
        default=AccountType.CLIENT
    )
    file = models.ImageField(upload_to=get_file_path, null=True, blank=True, verbose_name=_('Avatar'))
    activated_date = models.DateTimeField(default=timezone.now, null=False, blank=False, verbose_name=_('Activated date'))
    wallet_address = models.CharField(null=True,blank=True,max_length=50,verbose_name=_('Address of wallet'))

    def __str__(self):
        return str(self.email)

    class Meta:
        db_table = 'user'
        verbose_name = _('User')
        verbose_name_plural = _('Users')

class UserAction(Base):
    user = models.ForeignKey(User, verbose_name="User id", related_name="user_UserAction", on_delete=models.SET_NULL, null=True)
    action_type = models.PositiveIntegerField(
        verbose_name=_('ActionType'),
        choices=ActivityType.choices,
        default=ActivityType.ACTION
    )

    def __str__(self):
        return f"{self.user} made {self.action_type}"
    class Meta:
        db_table = 'user_action'
        verbose_name = _('UserAction')
        verbose_name_plural = _('UserActions')

def save_user(sender, instance, created, **kwargs):
    if created:
        pass



post_save.connect(save_user, sender=User)