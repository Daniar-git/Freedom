from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.db.models.signals import post_save, post_delete, pre_save
import django.dispatch
from nimble.user.models import *
from nimble.user.constants import *
from .models import Channel, VideoLikes, Video

def create_channel(sender, instance, created, **kwargs):

    if created:
        Channel.objects.create(user=instance, name=instance.username)
        UserAction.objects.create(user=instance,action_type=ActivityType.CREATE_CHANNEL)


def update_channel(sender, instance, **kwargs):

    if instance.id is not None:
        old_instance = User.objects.get(pk=instance.pk)

        if old_instance.username != instance.username:
            channel = Channel.objects.get(pk = instance.pk)
            channel.name = instance.username
            channel.save()
            UserAction.objects.create(user=instance, action_type=ActivityType.CHANGE_CHANNEL)


def delete_channel(sender, instance, **kwargs):
    UserAction.objects.create(user=instance, action_type=ActivityType.DELETE_CHANNEL)


def login(request, user, **kwargs):
    UserAction.objects.create(user=user, action_type=ActivityType.USER_LOGIN)

def logout(request, user, **kwargs):
    UserAction.objects.create(user=user, action_type=ActivityType.USER_LOGOUT)


video_watched = django.dispatch.Signal(providing_args=['video'])
liked_video = django.dispatch.Signal(providing_args=['video'])
value_liked_video = django.dispatch.Signal(providing_args=['video'])
fan_liked_video = django.dispatch.Signal(providing_args=['video'])
comment_video = django.dispatch.Signal(providing_args=['video', 'comment'])
post_save.connect(create_channel, sender=User)
pre_save.connect(update_channel, sender=User)
post_delete.connect(delete_channel, sender=User)
user_logged_in.connect(login)
user_logged_out.connect(logout)


