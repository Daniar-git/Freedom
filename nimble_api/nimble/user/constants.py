from django.db.models import IntegerChoices
from django.utils.translation import gettext_lazy as _


class AccountType(IntegerChoices):
    ADMIN = 0, _('Administrator')
    CLIENT = 1, _('Client')


class ActivityType(IntegerChoices):
    CREATE_CHANNEL = 0, _('Creat Channel')
    CHANGE_CHANNEL = 1, _('Change Channel')
    USER_LOGIN = 2, _('User login')
    USER_LOGOUT = 3, _('User logout')
    RESET_PASSWORD = 4,_('User reseted password')
    DELETE_CHANNEL = 5, _('User deleted channel')
    ACTION = 6, _('ACTION')
