from django.db import models
from nimble.common.models import Base
from django.contrib.auth.models import AbstractUser
from nimble.user.models import User
from nimble import settings
from django.utils.translation import gettext_lazy as _
from .constans import *
from uuid import uuid4
# Create your models here.

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    return 'videos/{}/{}.{}'.format(instance.pk, uuid4(), ext)

class Channel(Base):
    name = models.CharField(max_length=25, blank=False, verbose_name=_('name'))
    description = models.TextField(blank=True, verbose_name=_('description'))
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, verbose_name=_('user'), related_name='users', null=True)

    def __str__(self):
        return self.name
    class Meta:
         verbose_name_plural = "Channel"


class Playlist(Base):
    name = models.CharField(max_length=50, blank=False, verbose_name=_('name'))
    description = models.TextField(blank=True, verbose_name=_('description'))
    channel = models.ForeignKey(Channel, on_delete=models.SET_NULL, verbose_name=_('channel'), related_name='channels', null=True)

    def __str__(self):
        return str(self.name)
    
    class Meta:
         verbose_name_plural = "Playlist"


class Community(Base):
    name = models.CharField(max_length=50, blank=False, verbose_name=_('name'))
    channel = models.ForeignKey(Channel, on_delete=models.SET_NULL, verbose_name=_('channel'), related_name='communities', null=True)

    def __str__(self):
        return str(self.name)
    
    class Meta:
         verbose_name_plural = "Community"


class Tag(Base):
    name = models.CharField(max_length=50, blank=False, verbose_name=_('name'))

    def __str__(self):
        return str(self.name)
    
    class Meta:
         verbose_name_plural = "Tag"


class Video(Base):
    title = models.CharField(max_length=100, blank=False, verbose_name=_('title'))
    description = models.TextField(blank=True, verbose_name=_('description'))
    video = models.FileField(upload_to=get_file_path, null=True, blank=True, verbose_name=_('video'))
    views = models.IntegerField(null=True, blank=True, verbose_name=_('views'))
    category = models.PositiveIntegerField(choices = CATEGORIES.choices, verbose_name=_('category'))
    tags = models.ManyToManyField(Tag, verbose_name=_('tags'))
    is_private = models.BooleanField(verbose_name=_('is private'), default= False)
    playlist = models.ForeignKey(Playlist, on_delete=models.SET_NULL, blank=True, verbose_name=_('playlist'), related_name='videos', null=True)
    channel = models.ForeignKey(Channel, on_delete=models.SET_NULL, verbose_name=_('channel'), related_name='videos', null=True)
    like = models.PositiveIntegerField(verbose_name=_('common like'), default=0)
    value_like = models.PositiveIntegerField(verbose_name=_('value like'), default=0)
    fan_like = models.PositiveIntegerField(verbose_name=_('fan like'), default=0)

    def __str__(self):
        return str(self.title)
    
    class Meta:
         verbose_name_plural = "Video"

class VideoComment(Base):
    video = models.ForeignKey(Video, blank=True, on_delete=models.SET_NULL, verbose_name=_('video'), related_name='commented_video', null=True)
    user = models.ForeignKey(User, blank=True, on_delete=models.SET_NULL, verbose_name=_('user'), related_name='comment_user', null=True)
    comment = models.TextField(default='')
    class Meta:
        verbose_name_plural = "VideoComment"

class VideoWatches(Base):
    video = models.ForeignKey(Video, blank=True, on_delete=models.SET_NULL, verbose_name=_('video'),related_name='watched_video', null=True)
    user = models.ForeignKey(User, blank=True, on_delete=models.SET_NULL, verbose_name=_('user'),related_name='watch_user', null=True)

    class Meta:
        verbose_name_plural = "VideoWatches"

class VideoLikes(Base):
    user = models.ForeignKey(User, blank=True, on_delete=models.SET_NULL, verbose_name=_('user'),related_name='like_user', null=True)
    video = models.ForeignKey(Video, blank=True, on_delete=models.SET_NULL, verbose_name=_('video'),related_name='liked_video', null=True)
    like_type = models.PositiveIntegerField(
        verbose_name=_('LikeType'),
        choices=Like_Type.choices,
        default=Like_Type.CASUAL_LIKE
    )

    class Meta:
        verbose_name_plural = "Like"