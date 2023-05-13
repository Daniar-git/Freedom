from django.dispatch import receiver
from . import signals
from .models import *
from .constans import *
from nimble.user.models import *
from nimble.user.constants import *


@receiver(signals.video_watched)
def watched_video(sender, video, **kwargs):
    video= Video.objects.get(id=value)
    video.views = video.views+1
    user = User.objects.get(id=sender)
    Watches.objects.create(user=user, video=video)
    video.save()


@receiver(signals.liked_video)
def liked_video(sender, video, **kwargs):
    video = Video.objects.get(id=video)
    video.like = video.like + 1
    user = User.objects.get(id=sender)
    Likes.objects.create(user=user, video=video, like_type=Like_Type.CASUAL_LIKE)
    video.save()


@receiver(signals.value_liked_video)
def liked_video(sender, video, **kwargs):
    video = Video.objects.get(id=video)
    video.value_like = video.value_like + 1
    user = User.objects.get(id=sender)
    Likes.objects.create(user=user, video=video, like_type=Like_Type.VALUE_LIKE)
    video.save()


@receiver(signals.fan_liked_video)
def liked_video(sender, video, **kwargs):
    video = Video.objects.get(id=video)
    video.fan_like = video.fan_like + 1
    user = User.objects.get(id=sender)
    Likes.objects.create(user=user, video=video, like_type=Like_Type.FAN_LIKE)
    video.save()


@receiver(signals.comment_video)
def comment_vidoe(sender, video, comment, **kwargs):
    video = Video.objects.get(id=video)
    user = User.objects.get(id=sender)
    VideoComment.objects.create(video=video, user=user, comment=comment)