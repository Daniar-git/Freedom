from django.conf import settings
from django.utils import timezone

from rest_framework import permissions
from nimble.payment.models import Tariff


class CabinetAccessPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser or request.user.is_staff:
            return True
        subscription = request.user.subscription()
        if subscription.tariff != Tariff.objects.get(default=True):
            if subscription.expiry_date < timezone.now().date():
                return False
            return True
        else:
            if UserCourse.objects.filter(user=request.user).count() < settings.MAX_TEST_TRIES:
                return True
            else:
                return False