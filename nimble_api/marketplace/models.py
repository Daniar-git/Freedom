from django.db import models
from nimble.common.models import Base
from nimble.user.models import User
from main.models import *
from django.utils.translation import gettext_lazy as _

# Create your models here.

class NFTOwner(Base):
    user = models.ForeignKey(User, blank=True, on_delete=models.SET_NULL, verbose_name=_('nft_user'), related_name='nft_users', null=True)
    channel = models.ForeignKey(Channel, blank=True, on_delete=models.SET_NULL, verbose_name=_('nft_channel'), related_name='nft_channels', null=True)
    quantity = models.IntegerField(blank=True, verbose_name=_('quanitiy'), default=0)
    class Meta:
         verbose_name_plural = "NFT Owners"