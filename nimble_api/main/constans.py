from django.db import models
from django.db.models import IntegerChoices
from django.utils.translation import gettext_lazy as _

class CATEGORIES(IntegerChoices):
    EDUCATION = 0, _('Education')
    MUSIC = 1, _('Music')
    STREAMING = 2, _('Streaming')
    SOCIALMEDIA = 3, _('Social Media')
    GAMING = 4, _(' Gaming')
    MOVIE = 5, _('Movie')
    TRAVEL = 6, _('Travel')

class Like_Type(IntegerChoices):
    CASUAL_LIKE = 0, _('Common Like')
    FAN_LIKE = 1, _('Fan Like')
    VALUE_LIKE = 2, _('Value Like')